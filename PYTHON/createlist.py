def shopping_cart():
    cart = [100, 250, 75]

    if not cart:
        return "Cart is empty"

    print("Cart Items:", cart)

shopping_cart()