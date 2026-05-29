def get_salary(data, dept, emp):
    if dept in data and emp in data[dept]:
        print("Salary:", data[dept][emp])
    else:
        print("Employee not found")

employees = {
    "IT": {
        "Rahul": 60000,
        "Anu": 55000
    }
}

get_salary(employees, "IT", "Rahul")