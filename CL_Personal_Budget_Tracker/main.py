from budget import Budget
#Still runs in CL despite IDE issue.

def main():
    budget = Budget()

    while True:
        print("1. Add income")
        print("2. Add expense")
        print("3. Check balance")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter income amount: "))
            budget.add_income(amount)
        elif choice == "2":
            amount = float(input("Enter expense amount: "))
            budget.add_expense(amount)
        elif choice == "3":
            print(f"Current balance is: {budget.calculate_balance()}")
        elif choice == "4":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()