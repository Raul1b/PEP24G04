class Product:

    def __init__(self):
        self.name, self.price, self.stock = input("Give (name, price, stock) for product:").split(',')

    def __repr__(self):
        pass

    def __str__(self):
        pass

class Category:

    def __init__(self, name: str):
        self.category_name = name
        self.products = []

    def add_product(self):
        # product = input("give product:")
        product = Product()
        self.products.append(product)

class Shop:
    pass

