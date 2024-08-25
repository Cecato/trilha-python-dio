def print_statement(account):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not account.transactions else account.transactions)
    print(f"\nSaldo: R$ {account.balance:.2f}")
    print("==========================================")
