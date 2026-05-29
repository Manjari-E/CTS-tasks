students = {}

def add_grade(name, grade):
    if 0 <= grade <= 100:
        students.setdefault(name, []).append(grade)

def calculate_gpa(name):
    grades = students.get(name, [])

    if grades:
        return sum(grades) / len(grades)

add_grade("Arun", 80)
add_grade("Arun", 90)

print("GPA:", calculate_gpa("Arun"))