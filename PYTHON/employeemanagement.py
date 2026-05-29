import json

class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    def __str__(self):
        return f"{self.emp_id} - {self.name}"

employees = {
    1: Employee(1, "Arun"),
    2: Employee(2, "Priya")
}

data = {k: v.name for k, v in employees.items()}

with open("emps.json", "w") as f:
    json.dump(data, f)

with open("emps.json", "r") as f:
    loaded = json.load(f)

print(loaded)