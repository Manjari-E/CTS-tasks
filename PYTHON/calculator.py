def calculate(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a / b

try:
    a = float(input("Enter First Number: "))
    b = float(input("Enter Second Number: "))
    op = input("Enter Operator: ")

    print("Result =", calculate(a, b, op))

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Invalid Input")