"""Модели и логика для проекта интернет-магазина."""

from typing import List


class Product:
    """Класс, представляющий товар."""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Инициализация объекта."""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __str__(self) -> str:
        """Возвращает строковое представление объекта."""
        return f"{self.name}, {int(self.price)} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        """Позволяет складывать объекты Product по общей стоимости."""
        if not isinstance(other, Product):
            return NotImplemented
        return self.price * self.quantity + other.price * other.quantity


class Category:
    """Класс для представления категории товаров."""

    def __init__(self, name: str, description: str, products: List[Product]):
        """Инициализация объекта."""
        self.name = name
        self.description = description
        self._products = products

    @property
    def products(self) -> List[Product]:
        """Возвращает список продуктов в категории."""
        return self._products

    def __str__(self) -> str:
        """Возвращает строковое представление категории."""
        total_quantity = sum(product.quantity for product in self._products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."


class CategoryIterator:
    """Итератор для перебора товаров в категории."""

    def __init__(self, category: Category):
        """Инициализация объекта."""
        self._products = category.products
        self._index = 0

    def __iter__(self):
        """Возвращает итератор (self)."""
        return self

    def __next__(self) -> Product:
        """Возвращает следующий товар в категории."""
        if self._index < len(self._products):
            product = self._products[self._index]
            self._index += 1
            return product
        raise StopIteration
