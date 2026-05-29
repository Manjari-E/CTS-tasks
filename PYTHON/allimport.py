from math import *

def math_operations(num):
    if num < 0:
        return "Invalid input"

    print("Square Root:", sqrt(num))
    print("Power:", pow(num, 2))
    print("PI Value:", pi)

math_operations(4)