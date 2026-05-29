import math

def circle_area(radius):
    if radius <= 0:
        return "Invalid radius"

    area = math.pi * radius ** 2

    return f"Area: {area:.2f}"

print(circle_area(5))