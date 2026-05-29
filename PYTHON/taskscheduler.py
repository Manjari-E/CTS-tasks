from datetime import datetime

class Task:
    def __init__(self, name, due_date):
        self.name = name
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d")

tasks = [
    Task("Project", "2026-06-15"),
    Task("Assignment", "2026-06-01")
]

tasks.sort(key=lambda x: x.due_date)

for task in tasks:
    print(task.name, task.due_date.date())