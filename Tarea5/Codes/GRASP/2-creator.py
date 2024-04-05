class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ProductFactory:
    @staticmethod
    def create_product(name, price):
        return Product(name, price)


product = ProductFactory.create_product("Laptop", 999.99)
print(f"Producto creado: {product.name}, Precio: ${product.price}")
