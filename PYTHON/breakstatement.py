def first_even(limit):
    if limit <= 0:
        return "Invalid range"

    for i in range(limit):
        if i % 2 == 0:
            print("First even number:", i)
            break

first_even(10)