import datetime

def validar_data(pergunta, valor_atual=None):
    while True:
        data = input(pergunta).strip() or valor_atual

        if not data:
            print("\n>> ERRO: O campo de data não pode ficar em branco.")
            continue
               
        try:
            return datetime.datetime.strptime(data, "%Y-%m-%d").date()
        except ValueError:
            print("\n>> ERRO: Digite uma data válida (YYYY-MM-DD).")
            

def validar_data_devolucao(pergunta, valor_atual=None):
    while True:
        data = input(pergunta).strip()
        
        if data == "":
            return valor_atual

        try:
            return datetime.datetime.strptime(data, "%Y-%m-%d").date()
        except ValueError:
            print("\n>> ERRO: Digite uma data válida (YYYY-MM-DD).")


def validar_string(pergunta, valor_atual=None):
    while True:
        string = input(pergunta).strip().title() or valor_atual

        if not string:
            print("\n>> ERRO: O campo não pode estar vazio.")
            continue
        
        return string


def validar_int(pergunta, valor_atual=None):
    while True:
        numero = input(pergunta).strip() or valor_atual

        if numero is None:
            print("\n>> ERRO: O campo não pode estar vazio.")
            continue
        
        try:
            return int(numero)
        except ValueError:
            print("\n>> ERRO: Digite um número inteiro válido.")


def validar_isbn(pergunta, valor_atual=None):
    while True:
        isbn = input(pergunta).strip() or valor_atual

        if not isbn:
            print("\n>> ERRO: O ISBN não pode estar vazio.")
            continue       
        
        if len(isbn) == 13 and isbn.isdigit():  
            return isbn
        else:
            print("\n>> ERRO: O ISBN deve conter 13 dígitos numéricos.")