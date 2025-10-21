def mensagem_alerta(texto):
    print(f"\033[33m{texto}\033[0m")


def mensagem_erro(texto):
    print(f"\033[31m{texto}\033[0m")


def mensagem_sucesso(texto):
    print(f"\033[32m{texto}\033[0m")


def mensagem_informativa(texto):
    print(f"\033[36m\n{texto}\033[0m")   