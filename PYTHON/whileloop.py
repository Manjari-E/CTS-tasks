def countdown(count):
    if count <= 0:
        return "Invalid count"

    while count > 0:
        print(count)
        count -= 1

countdown(5)