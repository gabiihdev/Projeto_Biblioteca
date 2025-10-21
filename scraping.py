from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import sqlite3

URL = "https://pedrovncs.github.io/livrariapython/livros.html"
conn = sqlite3.connect("biblioteca.db")

def acessar_url():
    try:
        html = urlopen(URL)
    except Exception as ex:
        print(">> ERRO: acesso a URL")
        exit()
    return html


def exibir_cabecalho(bs):
    print(bs.h1.text)
    
    
def obter_lista(bs):
    lista = bs.find("ul", {"id":"livros-lista"}).find_all("li")
    return lista


def extrair_dados(lista_livros):
    dados = []
    
    for livro in lista_livros:
        titulo = livro.find("h5").text.strip()
        coluna = livro.find_all("p")
        isbn = coluna[0].text.replace("ISBN: ", "").strip()
        genero = coluna[1].text.replace("Gênero: ", "").strip()
        autor = coluna[2].text.replace("Autor(es): ", "").strip()
        pais = coluna[3].text.replace("País de Nascimento: ", "").strip()
        data_publicacao = coluna[4].text.replace("Data de publicação: ", "").strip()
        paginas = int(coluna[5].text.replace("Páginas: ", "").strip())
        quantidade = int(coluna[6].text.replace("Quantidade Disponível: ", "").strip())
        
        dados.append([titulo, isbn, genero, autor, pais, data_publicacao, paginas, quantidade])

    return pd.DataFrame(dados, columns=["Título", "ISBN", "Gênero", "Autor(es)", "País", "Data de Publicação", "Páginas", "Quantidade Disponível"])


html = acessar_url()
bs = BeautifulSoup(html, "html.parser")

exibir_cabecalho(bs)
lista_livros = obter_lista(bs)
df_livros = extrair_dados(lista_livros)


### FORMATAÇÃO DOS DADOS E CRIAÇÃO DOS DATAFRAMES

def formatar_data(df_livros): 
    df_livros["Data de Publicação"] = pd.to_datetime(df_livros["Data de Publicação"], format='mixed').dt.strftime("%Y-%m-%d")
    return df_livros


def formatar_paises(df_livros): 
    df_livros["País"] = df_livros["País"].str.split(", ").apply(set).str.join(", ")
    return df_livros
    
    
def criar_df_autores(df_livros):
    autores = df_livros[['Autor(es)', 'País']].copy()
    autores['Autor'] = autores['Autor(es)'].str.split(', ')
    autores = autores.explode('Autor')  
    autores = autores[['Autor', 'País']].drop_duplicates().reset_index(drop=True)
    
    return autores


def criar_df_livro_autor(df_livros, df_autores):
    livros_autores = []
    for _, livro_row in df_livros.iterrows():
        for _, autor_row in df_autores.iterrows():
            if autor_row['Autor'] in livro_row['Autor(es)']:
                livros_autores.append([livro_row['Título'], autor_row['Autor']])
    return pd.DataFrame(livros_autores, columns=['Título', 'Autor'])


formatar_data(df_livros)
formatar_paises(df_livros)
print(df_livros)

df_autores = criar_df_autores(df_livros)
print('\nDATAFRAME AUTORES:\n')
print(df_autores)

df_livro_autor = criar_df_livro_autor(df_livros, df_autores)
print('\nDATAFRAME LIVRO_AUTOR:\n')
print(df_livro_autor)


# INSERÇÃO DOS DATAFRAMES NO BANCO DE DADOS

def inserir_dados_bd(df_livros, df_autores, df_livro_autor):
    cursor = conn.cursor()

    for _, row in df_livros.iterrows():
        cursor.execute("""
        INSERT INTO livros (titulo, isbn, genero, data_publicacao, qtd_paginas, qtd_exemplares)
        VALUES (?, ?, ?, ?, ?, ?);
        """, (row['Título'], row['ISBN'], row['Gênero'], row['Data de Publicação'], row['Páginas'], row['Quantidade Disponível']))
    

    for _, row in df_autores.iterrows():
        cursor.execute("""
        INSERT INTO autores (nome, pais_origem)
        VALUES (?, ?);
        """, (row['Autor'], row['País']))
        
        
    for _, row in df_livro_autor.iterrows():
        cursor.execute("""
        INSERT INTO livros_autores (id_livro, id_autor)
        SELECT l.id_livro, a.id_autor
        FROM livros l
        JOIN autores a ON l.titulo = ? AND a.nome = ?
        """, (row['Título'], row['Autor']))
        
        
    conn.commit()
    print("\n>> DADOS INSERIDOS NO BANCO COM SUCESSO!!")


# EXIBIÇÃO DO DADOS QUE FORAM ADICIONADOS NO BANCO 

def verificar_insercao():
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM livros")
    livros = cursor.fetchall()
    print("\nTABELA LIVROS:\n")
    for livro in livros:
        print(livro)

    cursor.execute("SELECT * FROM autores")
    autores = cursor.fetchall()
    print("\nTABELA AUTORES:\n")
    for autor in autores:
        print(autor)
        
        
    cursor.execute("SELECT * FROM livros_autores")
    livros_autores = cursor.fetchall()
    print("\nTABELA LIVROS_AUTORES:\n")
    for livro_autor in livros_autores:
        print(livro_autor)


inserir_dados_bd(df_livros, df_autores, df_livro_autor) 
verificar_insercao()