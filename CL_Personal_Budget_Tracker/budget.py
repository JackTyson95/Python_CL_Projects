class Budget:
    def __init__(self):
        self.income = []
        self.expenses = []

    def add_income(self, amount):
        self.income.append(amount)

    def add_expense(self, amount):
        self.expenses.append(amount)

    def calculate_balance(self):
        return sum(self.income) - sum(self.expenses)