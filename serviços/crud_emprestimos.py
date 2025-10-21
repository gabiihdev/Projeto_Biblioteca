from database.crud_emprestimos_db import *
from utils.validacoes import *
from utils.mensagens import *
from tabulate import tabulate
import datetime

def realizar_emprestimo():
    id_usuario = validar_int("Digite o ID do usuário: ")
    id_livro = validar_int("Digite o ID do livro: ")
    data_emprestimo = datetime.datetime.now().strftime('%Y-%m-%d')
        
    if not verificar_usuario(id_usuario):
        mensagem_informativa("\n>> USUÁRIO NÃO ENCONTRADO.")
        return
        
    if not verificar_livro(id_livro):
        mensagem_informativa("\n>> LIVRO NÃO ENCONTRADO.")
        return
        
    if verificar_emprestimo(id_usuario, id_livro, emprestimo_aberto=True):
        mensagem_alerta("\n>> O USUÁRIO JÁ POSSUI UM EMPRÉSTIMO ABERTO COM ESTE LIVRO.")
        return
            
    if verificar_qtd_exemplares(id_livro) == 0:
        mensagem_alerta("\n>> NÃO HÁ EXEMPLARES DESTE LIVRO DISPONÍVEIS PARA EMPRÉSTIMO.")
        return
        
    realizar_emprestimo_db(id_usuario, id_livro, data_emprestimo)
    mensagem_sucesso("\n>> EMPRÉSTIMO REALIZADO COM SUCESSO!!")


def encerrar_emprestimo():
    id_usuario = validar_int("Digite o ID do usuário: ")
    id_livro = validar_int("Digite o ID do livro: ")
    data_devolucao = datetime.datetime.now().strftime('%Y-%m-%d')
        
    if not verificar_emprestimo(id_usuario, id_livro, emprestimo_aberto=True):
        mensagem_informativa(">> EMPRÉSTIMO NÃO ENCONTRADO.")
        return
    
    encerrar_emprestimo_db(id_usuario, id_livro, data_devolucao)
    mensagem_sucesso("\n>> EMPRÉSTIMO ENCERRADO COM SUCESSO!!")
        
        
def listar_emprestimos():
    emprestimos = listar_todos_emprestimos()
        
    if not emprestimos:
        mensagem_informativa(">> NENHUM EMPRÉSTIMO REALIZADO")        
    else:
        headers = ["ID do Livro", "Título", "ID do Usuário", "Nome", "Sobrenome", "Data de Empréstimo", "Data de Devolução"]
        print(tabulate(emprestimos, headers=headers, tablefmt="fancy_grid"))   
            

def atualizar_emprestimo():
    id_usuario = validar_int("Digite o ID do usuário do empréstimo: ")
    id_livro = validar_int("Digite o ID do livro do empréstimo: ")
        
    emprestimo_existente = verificar_emprestimo(id_usuario, id_livro, emprestimo_aberto=False)
        
    if not emprestimo_existente:
        mensagem_informativa("\n>> EMPRÉSTIMO NÃO ENCONTRADO.")
        return
        
    else:
        print("\n** Pressione ENTER para manter o valor atual.\n")    
        novo_id_livro = validar_int("Digite o ID do novo livro: ", emprestimo_existente[0])
        novo_id_usuario = validar_int("Digite o ID do novo usuário: ", emprestimo_existente[1])
        nova_data_emprestimo = validar_data("Digite a nova data do empréstimo (YYYY-MM-DD): ", emprestimo_existente[2])
        nova_data_devolucao = validar_data_devolucao("Digite a nova data de devolução (YYYY-MM-DD): ", emprestimo_existente[3])
            
        if not verificar_livro(novo_id_livro):
            mensagem_informativa("\n>> NOVO LIVRO NÃO ENCONTRADO.")
            return
            
        if not verificar_usuario(novo_id_usuario):
            mensagem_informativa("\n>> NOVO USUÁRIO NÃO ENCONTRADO.")
            return
            
        atualizar_emprestimos_db(novo_id_usuario, novo_id_livro, nova_data_emprestimo, nova_data_devolucao, id_usuario, id_livro)
        mensagem_sucesso("\n>> EMPRÉSTIMO ATUALIZADO COM SUCESSO.")
        

def deletar_emprestimo():
    id_usuario = validar_int("Digite o ID do usuário do empréstimo: ")
    id_livro = validar_int("Digite o ID do livro do empréstimo: ")
        
    if not verificar_usuario(id_usuario):
        mensagem_informativa("\n>> USUÁRIO NÃO ENCONTRADO.")
        return
        
    if not verificar_livro(id_livro):
        mensagem_informativa("\n>> LIVRO NÃO ENCONTRADO.")
        return
        
    if verificar_emprestimo(id_usuario, id_livro, emprestimo_aberto=True):
        mensagem_alerta("\n>> O EMPRÉSTIMO AINDA ESTÁ ABERTO E NÃO PODE SER DELETADO.")
        return
        
    confirm = input("\n** TEM CERTEZA DE QUE DESEJA DELETAR ESTE EMPRÉSTIMO (s/n)? ").strip().lower()
    if confirm == "n":
        mensagem_erro("\n>> OPERAÇÃO CANCELADA.")
        return
    
    else:
        deletar_emprestimos_db(id_usuario, id_livro)
        mensagem_sucesso("\n>> EMPRÉSTIMO DELETADO COM SUCESSO.")