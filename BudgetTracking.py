# Define a function to start the budget tracking program
# This function initializes the budget, presents a menu to the user, and handles user input.
def StartBudgetTracking():
    currentBudget = float(input("Please enter your current budget: "))
    budget = currentBudget
    expensesList = []

    while True:
        print("\nWelcome, track your budget, what would you like to do?")
        print("0. Exit")
        print("1. Show Current Budget Details")
        print("2. Add Expense")
        print("3. Deposit")
        choice = input("Enter your choice: (1/2/3/4) and 0 for Exit: ")

        if choice == "0":
            break
        elif choice == "1":
            showBudgetDetails(budget, expensesList)
        elif choice == "2":
            description = input("Enter expense description: ")
            amount = float(input("Enter expense amount: "))
            addExpense(expensesList,description,amount)
        elif choice == "3":
            print("Your current budget: " + str(currentBudget))
            addBudget = float(input("How much do you want to add (only numbers): "))
            currentBudgetPlaceHolder = currentBudget
            budget += addBudget
            print("You added " + str(addBudget) + " to " + str(currentBudgetPlaceHolder) + " your new total budget is " + str(budget))

# Define a function to add an expense to the expenses list
# This function takes in the expenses list, expense description, and expense amount, and adds the expense to the list.
def addExpense(expenses, description, amount):
    expenses.append({"description": description, "amount": amount})
    print(f"Added expense: {description}, amount: {amount}")

# Define a function to show the current budget details
# This function takes in the budget and expenses list, and prints out the total budget, expenses, total spent, and remaining budget.
def showBudgetDetails(budget, expensesList):
    print(f"Deposited Total budget: {budget}")
    print("Expenses:")
    for expense in expensesList:
        print(f"Description: {expense['description']}, Amount: {expense['amount']}")
    print(f"Total spent: {GetTotalExpenses(expensesList)}")
    print(f"Remaining Budget: {GetBalance(budget,expensesList)}")

# Define a function to calculate the total expenses
# This function takes in the expenses list, and returns the total expenses.
def GetTotalExpenses(expensesList):
    sum = 0
    for expense in expensesList:
        sum += expense["amount"]
    return sum

# Define a function to calculate the remaining budget
# This function takes in the budget and expenses list, and returns the remaining budget.
def GetBalance(budget, expensesList):
    return budget - GetTotalExpenses(expensesList)