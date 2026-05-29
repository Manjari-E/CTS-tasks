class Employee:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Employee Name:", self.name)

emp1 = Employee("Arun")
emp2 = Employee("Priya")
emp3 = Employee("Rahul")

emp1.display()
emp2.display()
emp3.display()