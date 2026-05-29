class Employee:
    def __init__(self, name):
        self.name = name
        self.salary = 0

    def set_salary(self, salary):
        if salary > 0:
            self.salary = salary
        return self

    def apply_raise(self, amount):
        self.salary += amount
        return self

    def display(self):
        print(f"{self.name} Salary: {self.salary}")
        return self

emp = Employee("Arun")
emp.set_salary(50000).apply_raise(5000).display()