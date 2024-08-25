class Account:
    def __init__(self, balance=0, limit=500, max_withdrawals=3):
        self.balance = balance
        self.limit = limit
        self.transactions = ""
        self.withdrawal_count = 0
        self.max_withdrawals = max_withdrawals

    def add_transaction(self, description: str, amount: float):
        self.transactions += f"{description}: R$ {amount:.2f}\n"