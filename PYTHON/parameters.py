def add(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "Invalid input"

    return a + b

print("Sum:", add(5, 3))