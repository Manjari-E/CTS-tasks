def print_numbers(count):
    if count <= 0:
        return "Invalid count"

    for i in range(count):
        print(i + 1)

print_numbers(5)