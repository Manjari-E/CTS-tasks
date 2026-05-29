def salary_details(salaries):
    if not salaries:
        return "Salary list is empty"

    print("Highest Salary:", max(salaries))
    print("Lowest Salary:", min(salaries))

salary_list = [50000, 75000, 62000, 95000]

salary_details(salary_list)