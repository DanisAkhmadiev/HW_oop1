import json
class Product:
    name: str
    description: str
    price: float
    available: int
    all_unique_prod = []

    def __init__(self, name, description, price, available):
        self.name = name
        self.description = description
        self.price = price
        self.available = available
        self.add_to_unique_products()

    def add_to_unique_products(self):
        '''Добавляет в список всех продуктов новый продукт'''
        if self.name not in Product.all_unique_prod:
            Product.all_unique_prod.append(self.name)


class Category:
    name: str
    description: str
    products = list
    total_categories = 0
    total_unique_products = 0

    @staticmethod
    def update_unique_products():
        Category.total_unique_products = len(Product.all_unique_prod)



    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        Category.total_categories += 1



# p1 = Product('hbrslfn', 'sgvdl', 130, 48)
# p2 = Product('jhvxfku', 'jdbfjh', 94, 84)
# Category.update_unique_products()
# print(Category.total_unique_products)
#
