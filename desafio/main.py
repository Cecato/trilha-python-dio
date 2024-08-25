from models.account import Account
from services.deposit import deposit
from services.withdraw import withdraw
from services.statement import print_statement

def main():
    account = Account()

    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """

    while True:
        option = input(menu).lower()

        if option == "d":
            amount = float(input("Informe o valor do depósito: "))
            deposit(account, amount)

        elif option == "s":
            amount = float(input("Informe o valor do saque: "))
            withdraw(account, amount)

        elif option == "e":
            print_statement(account)

        elif option == "q":
            print("Saindo do sistema. Obrigado por usar o Banco Python!")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


if __name__ == "__main__":
    main()
