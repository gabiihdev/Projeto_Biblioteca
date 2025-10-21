from database.crud_usuarios_db import *
from tabulate import tabulate
from utils.validacoes import *
from utils.mensagens import *
from tabulate import tabulate

def cadastrar_usuario():
    nome = validar_string("Digite o nome do usuário: ")
    sobrenome = validar_string("Digite o sobrenome do usuário: ")
    data_nascimento = validar_data("Digite a data de nascimento do usuário (YYYY-MM-DD): ")
        
    if verificar_usuario(nome, sobrenome, data_nascimento):
        mensagem_alerta("\n>> JÁ EXISTE UM USUÁRIO CADASTRADO COM ESSAS INFORMAÇÕES.") 
                 
    else:
        cadastrar_usuario_db(nome, sobrenome, data_nascimento)
        mensagem_sucesso(f"\n>> USUÁRIO '{nome} {sobrenome}' CADASTRADO COM SUCESSO!!")
        
        
def listar_usuarios():
    usuarios = listar_usuarios_db()
        
    if not usuarios:
        mensagem_informativa(">> NENHUM USUÁRIO CADASTRADO.")
    else:
        headers = ["ID", "Nome", "Sobrenome", "Data de Nascimento", "Empréstimos"]
        print(tabulate(usuarios, headers=headers, tablefmt="fancy_grid"))

        
def buscar_usuario():
    usuario = input("Digite o nome completo ou o ID do usuário que deseja: ").strip().title() 
    usuario_encontrado = buscar_usuario_db(usuario)
        
    if not usuario_encontrado:
        mensagem_informativa(">> USUÁRIO NÃO ENCONTRADO.")
        return None
    else:
        print()
        headers = ["ID", "Nome", "Sobrenome", "Data de Nascimento", "Empréstimos"]
        print(tabulate([usuario_encontrado], headers=headers, tablefmt="fancy_grid"))
        return usuario_encontrado
        

def atualizar_usuario():
    usuario = buscar_usuario()
    if not usuario:  
        return

    print("\n>> Pressione ENTER para manter o valor atual.\n")
    novo_nome = validar_string("Digite o novo nome do usuário: ", usuario[1])
    novo_sobrenome = validar_string("Digite o novo sobrenome do usuário: ", usuario[2])
    nova_data_nascimento = validar_data("Digite a nova data de nascimento do usuário (YYYY-MM-DD): ", usuario[3])
            
    if verificar_usuario(novo_nome, novo_sobrenome, nova_data_nascimento, usuario[0]):
        mensagem_alerta("\n>> JÁ EXISTE UM USUÁRIO CADASTRADO COM ESSAS INFORMAÇÕES.")
        return

    else:
        atualizar_usuario_db(novo_nome, novo_sobrenome, nova_data_nascimento, usuario[0])
        mensagem_sucesso(f"\n>> USUÁRIO '{usuario[1]}' ATUALIZADO COM SUCESSO!!")
        

def deletar_usuario():
    usuario = buscar_usuario()
    if not usuario:
        return

    if verificar_emprestimo_aberto(usuario[0]):
        mensagem_alerta("\n>> ESTE USUÁRIO POSSUI EMPRÉSTIMOS ABERTOS E NÃO PODE SER DELETADO.")
        return
        
    else:
        confirm = input("\n** TEM CERTEZA DE QUE DESEJA DELETAR ESTE USUÁRIO (s/n)? ").strip().lower()
            
        if confirm == "n":
            mensagem_erro("\n>> OPERAÇÃO CANCELADA.")
            return
        else:
            remover_usuario(usuario[0])
            mensagem_sucesso(f"\n>> USUÁRIO '{usuario[1]}' DELETADO COM SUCESSO!!")