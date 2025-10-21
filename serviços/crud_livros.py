from database.crud_livros_db import *
from utils.validacoes import *
from utils.mensagens import *
from tabulate import tabulate

def cadastrar_livro():
    titulo = validar_string("Digite o título do livro: ")
    isbn = validar_isbn("Digite o ISBN (13 dígitos): ")
    genero = validar_string("Digite o gênero do livro: ")
    data_publicacao = validar_data("Digite a data de publicação do livro (YYYY-MM-DD): ")
    qtd_paginas = validar_int("Digite a quantidade de páginas do livro: ")
    qtd_exemplares = validar_int("Digite a quantidade de exemplares do livro: ")

    if verificar_livro(isbn, titulo):
        mensagem_alerta("\n>> JÁ EXISTE UM LIVRO CADASTRADO COM ESSAS INFORMAÇÕES.")
        return
    else:
        cadastrar_livro_db(titulo, isbn, genero, data_publicacao, qtd_paginas, qtd_exemplares)
        mensagem_sucesso(f"\n>> LIVRO '{titulo}' CADASTRADO COM SUCESSO!!")        
    
    
def listar_livros():
    livros = listar_livros_db()

    if not livros:
        mensagem_informativa(">> NENHUM LIVRO CADASTRADO")
        return
    else:
        headers = ["ID", "Título", "ISBN", "Gênero", "Data de Publicação", "Páginas", "Disponíveis"]
        print(tabulate(livros, headers=headers, tablefmt="fancy_grid"))

        
def buscar_livro():
    livro = input("Digite o título ou o ID do livro que deseja: ").strip()
    livro_encontrado = buscar_livro_db(livro)
    
    if not livro_encontrado:
        mensagem_informativa("\n>> NENHUM LIVRO ENCONTRADO.")
        return None
    else:
        print()
        headers = ["ID", "Título", "ISBN", "Gênero", "Data de Publicação", "Qtd. Páginas", "Qtd. Exemplares"]
        print(tabulate([livro_encontrado], headers=headers, tablefmt="fancy_grid"))
        return livro_encontrado
        

def atualizar_livro():
    livro = buscar_livro()
    if not livro:
        return
    
    print("\n>> Pressione ENTER para manter o valor atual.\n")    
    novo_titulo = validar_string("Digite o novo título: ", livro[1])
    novo_isbn = validar_isbn("Digite o novo ISBN: ", livro[2])
    novo_genero = validar_string("Digite o novo gênero: ", livro[3])
    nova_data_publicacao = validar_data("Digite a nova data de publicação (YYYY-MM-DD): ", livro[4])
    nova_qtd_paginas = validar_int("Digite a nova quantidade de páginas: ", livro[5])
    nova_qtd_exemplares = validar_int("Digite a nova quantidade de exemplares: ", livro[6])

    if verificar_livro(novo_isbn, novo_titulo, livro[0]):
        mensagem_alerta(f"\n>> JÁ EXISTE UM LIVRO CADASTRADO COM O TÍTULO '{novo_titulo}' E ISBN '{novo_isbn}'.")
        return
    else:
        atualizar_livro_db(novo_titulo, novo_isbn, novo_genero, nova_data_publicacao, nova_qtd_paginas, nova_qtd_exemplares, livro[0])
        mensagem_sucesso(f"\n>> LIVRO '{novo_titulo}' ATUALIZADO COM SUCESSO!!")
        

def deletar_livro():
    livro = buscar_livro()
    if not livro:
        return
    
    if verificar_emprestimo_aberto(livro[0]):
        mensagem_alerta("\n>> ESTE LIVRO NÃO PODE SER DELETADO PORQUE ESTÁ EMPRESTADO.")
        return
        
    else:
        confirm = input("\n** TEM CERTEZA DE QUE DESEJA DELETAR ESTE LIVRO (s/n)? ").strip().lower()
            
        if confirm == "n":
            mensagem_erro("\n>> OPERAÇÃO CANCELADA.")
        else:
            deletar_livro_db(livro[0])
            mensagem_sucesso(f"\n>> LIVRO '{livro[1]}' DELETADO COM SUCESSO!!")   