import json
class Category:
    name: str
    description: str
    products = list
    total_categories = 0
    total_unique_products = 0



    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        Category.total_categories += 1

class Product:
    name: str
    description: str
    price: float
    available: int

    def __init__(self, name, description, price, available):
        self.name = name
        self.description = description
        self.price = price
        self.available = available
        Category.total_unique_products += 1

all_prod_cat = []
all_cat_prod = []

with open('products.json', 'r') as file:
    data = json.load(file)

for category in data:
    prod_cat = Category(category['name'], category["description"], category["products"])
    all_prod_cat.append(prod_cat)
    for product in category['products']:
        cat_prod = Product(product['name'], product["description"], product["price"], product["quantity"])
    all_cat_prod.append(cat_prod)

print(prod_cat.total_categories)

print(prod_cat.total_unique_products)


