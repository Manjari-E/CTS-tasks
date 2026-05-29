from tabulate import tabulate

c = float(input("Enter Celsius: "))

f = (c * 9/5) + 32
k = c + 273.15

table = [
    ["Celsius", c],
    ["Fahrenheit", round(f, 2)],
    ["Kelvin", round(k, 2)]
]

print(tabulate(table, headers=["Unit", "Value"]))