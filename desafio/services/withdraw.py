def withdraw(account, amount):
    if amount <= 0:
        print("Operação falhou! O valor informado é inválido.")
    elif amount > account.balance:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif amount > account.limit:
        print("Operação falhou! O valor do saque excede o limite.")
    elif account.withdrawal_count >= account.max_withdrawals:
        print("Operação falhou! Número máximo de saques excedido.")
    else:
        account.balance -= amount
        account.add_transaction("Saque", -amount)
        account.withdrawal_count += 1
        print(f"Saque de R$ {amount:.2f} realizado com sucesso!")
