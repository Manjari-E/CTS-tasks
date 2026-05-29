def add_expense():
    expenses = [500, 1200, 300]
    new_expense = 700

    if new_expense > 0:
        expenses.append(new_expense)

    print("Updated Expenses:", expenses)

add_expense()