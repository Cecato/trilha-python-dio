from models.user import User
from utils.validators import validar_cpf
from utils.user_filter import filtrar_usuario

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    
    if not validar_cpf(cpf):
        print("\n@@@ CPF inválido! @@@")
        return

    if filtrar_usuario(cpf, usuarios):
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append(User(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco))

    print("=== Usuário criado com sucesso! ===")



