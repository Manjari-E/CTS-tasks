class Product:
    def __init__(self, name):
        self.name = name

class Perishable(Product):
    pass

class Electronics(Product):
    pass

inventory = {
    "Milk": 5,
    "Laptop": 20,
    "Bread": 3
}

low_stock = {item for item, qty in inventory.items() if qty < 10}

print("Inventory:", inventory)
print("Low Stock Alert:", low_stock)