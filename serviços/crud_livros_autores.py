from database.crud_livros_autores_db import *
from utils.validacoes import *
from utils.mensagens import *
from tabulate import tabulate

def vincular_livro_autor():
        print("_" * 100)
        id_livro = validar_int("Digite o ID do livro que deseja vincular: ")
        id_autor = validar_int("Digite o ID do autor que deseja vincular: ")
        
        if not verificar_livro(id_livro):
            mensagem_informativa(">> LIVRO NÃO ENCONTRADO.")
            return

        if not verificar_autor(id_autor):
            mensagem_informativa(">> AUTOR NÃO ENCONTRADO.")
            return
        
        if verificar_vinculo(id_livro, id_autor):
            mensagem_alerta("\n>> ESTE LIVRO JÁ ESTÁ VICULADO A ESTE AUTOR.")
            return           
        
        vincular_livro_autor_db(id_livro, id_autor)
        mensagem_sucesso(f"\nLIVRO {id_livro} VINCULADO A AUTOR {id_autor} CON SUCESSO!!")
        
        
def buscar_livro_autor():
    print("_" * 100)
    autor = input("Digite o nome ou ID do autor que deseja: ").strip().title()
    livros_autor_encontrados = buscar_livro_autor_db(autor)
        
    if not livros_autor_encontrados:
        mensagem_informativa("\n>> NENHUM LIVRO ENCONTRADO.")
        return
    else:
        headers = ["ID do Livro", "Título", "ISBN", "Data de Publicação", "Gênero", "Qtd. Páginas", "Qtd. Exemplares", "Autor"]
        print(tabulate(livros_autor_encontrados, headers=headers, tablefmt="fancy_grid"))