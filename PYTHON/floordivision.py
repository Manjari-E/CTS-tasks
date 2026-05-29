def split_bill(total_bill, people):
    if total_bill <= 0 or people <= 0:
        return "Invalid input"

    share = total_bill // people

    return f"Each person pays: {share}"

total_bill = 1250
people = 4

print(split_bill(total_bill, people))