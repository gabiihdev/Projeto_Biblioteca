from serviços.crud_usuarios import *
from serviços.crud_livros import *
from serviços.crud_emprestimos import *
from serviços.crud_autores import *
from serviços.crud_livros_autores import *

def menu_principal():
    while True:
        print("_" * 100)
        print("╔════════════════════════════════════════════════════╗")
        print("║           GERENCIAMENTO DA BIBLIOTECA              ║")
        print("╚════════════════════════════════════════════════════╝")
        print("[1] - Gerenciar Usuários")
        print("[2] - Gerenciar Livros")
        print("[3] - Gerenciar Empréstimos")
        print("[4] - Gerenciar Autores")
        print("[5] - Vincular Livros a Autores")
        print("[6] - Buscar Livros de Autores")
        print("[0] - Sair")
        
        opcao = input("\nESCOLHA UMA OPÇÃO: ")
        
        match opcao:
            case "1":
                menu_usuarios()
            case "2":
                menu_livros()
            case "3":
                menu_emprestimos()
            case "4":
                menu_autores()
            case "5":
                vincular_livro_autor()
            case "6":
                buscar_livro_autor()
            case"0":
                print("\n>> Programa Encerrado.")
                break
            case _:
                print("\033[31m \n>> OPÇÃO INVÁLIDA \033[0m")
            
            
def menu_usuarios():
    while True:
        print("_" * 100)
        print("╔════════════════════════════════════════════════════╗")
        print("║            GERENCIAMENTO DE USUÁRIOS               ║")
        print("╚════════════════════════════════════════════════════╝")
        print("[1] - Cadastrar Usuários")
        print("[2] - Listar Usuários")
        print("[3] - Buscar Usuários")
        print("[4] - Atualizar Usuários")
        print("[5] - Deletar Usuários")
        print("[0] - Voltar para o menu principal")
        
        opcao = input("\nESCOLHA UMA OPÇÃO: ")
        print("_" * 100)
        
        match opcao:
            case "1":
                cadastrar_usuario()
            case "2":
                listar_usuarios()
            case "3":
                buscar_usuario()
            case "4":
                atualizar_usuario()
            case "5":
                deletar_usuario()
            case "0":
                print("\n>> Voltando para o menu principal...")
                break
            case _:
                print("\033[31m \n>> OPÇÃO INVÁLIDA \033[0m")            
       
            
def menu_livros():
    while True:
        print("_" * 100)
        print("╔════════════════════════════════════════════════════╗")
        print("║             GERENCIAMENTO DE LIVROS                ║")
        print("╚════════════════════════════════════════════════════╝")
        print("[1] - Cadastrar Livros")
        print("[2] - Listar Livros")
        print("[3] - Buscar Livros")
        print("[4] - Atualizar Livros")
        print("[5] - Deletar Livros")
        print("[0] - Voltar para o menu principal")
        
        opcao = input("\nESCOLHA UMA OPÇÃO: ")
        print("_" * 100)
        
        match opcao:
            case "1":
                cadastrar_livro()
            case "2":
                listar_livros()
            case "3":
                buscar_livro()
            case "4":
                atualizar_livro()
            case "5":
                deletar_livro()
            case "0":
                print(">> Voltando para o menu principal...")
                break
            case _:
                print("\033[31m \n>> OPÇÃO INVÁLIDA \033[0m")    


def menu_emprestimos():
    while True:
        print("_" * 100)
        print("╔════════════════════════════════════════════════════╗")
        print("║           GERENCIAMENTO DE EMPRÉSTIMOS             ║")
        print("╚════════════════════════════════════════════════════╝")        
        print("[1] - Realizar Empréstimos")
        print("[2] - Encerrar Empréstimos (Devoluções)")
        print("[3] - Listar Empréstimos")
        print("[4] - Atualizar Empréstimos")
        print("[5] - Deletar Empréstimos")
        print("[0] - Voltar para o menu principal")
        
        opcao = input("\nESCOLHA UMA OPÇÃO: ")
        print("_" * 100)
        
        match opcao:
            case "1":
                realizar_emprestimo()
            case "2":
                encerrar_emprestimo()
            case "3":
                listar_emprestimos()
            case "4":
                atualizar_emprestimo()
            case "5":
                deletar_emprestimo()
            case "0":
                print("\n>> Voltando para o menu principal...")
                break
            case _:
                print("\033[31m \n>> OPÇÃO INVÁLIDA \033[0m")            


def menu_autores():
    while True:
        print("_" * 100)
        print("╔════════════════════════════════════════════════════╗")
        print("║             GERENCIAMENTO DE AUTORES               ║")
        print("╚════════════════════════════════════════════════════╝")
        print("[1] - Cadastrar Autores")
        print("[2] - Listar Autores")
        print("[3] - Buscar Autores")
        print("[4] - Atualizar Autores")
        print("[5] - Deletar Autores")
        print("[0] - Voltar para o menu principal")
        
        opcao = input("\nESCOLHA UMA OPÇÃO: ")
        print("_" * 100)
        
        match opcao:
            case "1":
                cadastrar_autor()
            case "2":
                listar_autores()
            case "3":
                buscar_autor()
            case "4":
                atualizar_autor()
            case "5":
                deletar_autor()
            case "0":
                print("\n>> Voltando para o menu principal...")
                break
            case _:
                print("\033[31m \n>> OPÇÃO INVÁLIDA \033[0m")                
         
            
menu_principal()