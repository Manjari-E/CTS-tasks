import matplotlib.pyplot as plt

class Category:
    def __init__(self, name, limit):
        self.name = name
        self.limit = limit
        self.spent = 0

food = Category("Food", 5000)
food.spent = 6000

if food.spent > food.limit:
    print("Budget Exceeded")

labels = ["Food"]
amounts = [food.spent]

plt.pie(amounts, labels=labels)
plt.title("Monthly Budget")
plt.show()