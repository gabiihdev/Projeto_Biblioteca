from database.crud_autores_db import *
from utils.validacoes import *
from utils.mensagens import *
from tabulate import tabulate

def cadastrar_autor():
    nome = validar_string("Digite o nome do autor: ")
    pais_origem = validar_string("Digite o país de origem do autor: ")
        
    if verificar_autor(nome, pais_origem):
        mensagem_alerta("\n>> JÁ EXISTE UM AUTOR CADASTRADO COM ESSAS INFORMAÇÕES.")
        return
        
    else:            
        cadastrar_autor_db(nome, pais_origem)
        mensagem_sucesso(f"\n>> AUTOR '{nome}' CADASTRADO COM SUCESSO!!")
        
        
def listar_autores():
    autores = listar_autores_db()
        
    if not autores:
        mensagem_informativa("\n>> NENHUM AUTOR CADASTRADO.")
    else:
        headers = ["ID", "Nome", "País de Origem", "Livros"]
        print(tabulate(autores, headers=headers, tablefmt="fancy_grid"))
        

def buscar_autor():
    autor = input("Digite o nome ou o ID do autor que deseja: ").strip()
    autor_encontrado = buscar_autor_db(autor)

    if not autor_encontrado:
        mensagem_informativa(">> AUTOR NÃO ENCONTRADO.")
        return None
    else:
        print()
        headers = ["ID", "Nome", "País de Origem", "Livros"]
        print(tabulate([autor_encontrado], headers=headers, tablefmt="fancy_grid"))
        return autor_encontrado 


def atualizar_autor():
    autor = buscar_autor()
    if not autor:
        return
    
    print("\n** Pressione ENTER para manter o valor atual.\n")
    novo_nome = validar_string("Digite o novo nome: ", autor[1])
    novo_pais_origem = validar_string("Digite o novo país de origem: ", autor[2])
            
    if verificar_autor(novo_nome, novo_pais_origem, autor[0]):
        mensagem_alerta("\n>> JÁ EXISTE UM AUTOR CADASTRADO COM ESSAS INFORMAÇÕES.")
        return                
            
    else:
        atualizar_autor_db(novo_nome, novo_pais_origem, autor[0])
        mensagem_sucesso(f"\n>> AUTOR '{novo_nome}' ATUALIZADO COM SUCESSO!!")
                
        
def deletar_autor():
    autor = buscar_autor()
    if not autor:
        return
    
    confirm = input("\n** TEM CERTEZA DE QUE DESEJA DELETAR ESTE AUTOR (s/n)? ").strip().lower()
            
    if confirm == "n":
        mensagem_erro("\n>> OPERAÇÃO CANCELADA.")
            
    else:
        remover_autor(autor[0])
        mensagem_sucesso(f"\n>> AUTOR '{autor[1]}' DELETADO COM SUCESSO!!")