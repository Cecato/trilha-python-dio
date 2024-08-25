def deposit(account, amount):
    if amount > 0:
        account.balance += amount
        account.add_transaction("Depósito", amount)
        print(f"Depósito de R$ {amount:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
