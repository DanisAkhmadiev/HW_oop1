import pytest
from main.functions import Category, Product
@pytest.fixture
def pizza_category():
    return Category('Pizzas', 'pizza products', ["Margarita"])
@pytest.fixture
def pizza_margarita():
    return Product('Margarita', 'classical pizza with tomatos', 450, 30)
def test_init_category(pizza_category):
    assert pizza_category.name == 'Pizzas'
    assert pizza_category.description == 'pizza products'
    assert pizza_category.products == ['Margarita']
    assert Category.total_categories == 1
    assert Category.total_unique_products == 1
def test_init_product(pizza_margarita):
    assert pizza_margarita.name == 'Margarita'
    assert pizza_margarita.description == 'classical pizza with tomatos'
    assert pizza_margarita.price == 450
    assert pizza_margarita.available == 30




