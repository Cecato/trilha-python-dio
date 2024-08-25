from models.account import Account
from utils.user_filter import filtrar_usuario

def criar_conta(agencia, numero_conta, usuarios):
    from utils.validators import validar_cpf
    cpf = input("Informe o CPF do usuário: ")
    
    if not validar_cpf(cpf):
        print("\n@@@ CPF inválido! @@@")
        return None

    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return Account(agencia=agencia, numero_conta=numero_conta, usuario=usuario)

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")


def listar_contas(contas):
    from utils.menu import formatar_conta
    for conta in contas:
        print(formatar_conta(conta))