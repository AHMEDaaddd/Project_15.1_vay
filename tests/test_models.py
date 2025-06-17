from src.models import Category, CategoryIterator, Product


def test_product_str():
    p = Product("Test", "Test desc", 100.0, 5)
    assert str(p) == "Test, 100 руб. Остаток: 5 шт."


def test_category_str():
    p1 = Product("A", "desc", 100.0, 5)
    p2 = Product("B", "desc", 200.0, 10)
    c = Category("Phones", "desc", [p1, p2])
    assert str(c) == "Phones, количество продуктов: 15 шт."


def test_product_addition():
    p1 = Product("A", "desc", 100.0, 2)
    p2 = Product("B", "desc", 300.0, 1)
    assert p1 + p2 == 500.0


def test_category_iterator():
    p1 = Product("A", "desc", 100.0, 2)
    p2 = Product("B", "desc", 300.0, 1)
    category = Category("TestCat", "desc", [p1, p2])
    iterator = CategoryIterator(category)
    products = list(iterator)
    assert products == [p1, p2]
