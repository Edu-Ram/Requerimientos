class ShoppingCart:
    def __init__(self, items=[]):
        self.items = items

    def add_item(self, item):
        self.items.append(item)


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


product = Product("Laptop", 999.99)
cart = ShoppingCart()
cart.add_item(product)
