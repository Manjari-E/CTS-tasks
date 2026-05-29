def calculate_grade(score):
    if score < 0 or score > 100:
        return "Invalid score"

    if score >= 90:
        return "Grade A"
    elif score >= 70:
        return "Grade B"
    else:
        return "Grade C"

score = 88

print(calculate_grade(score))