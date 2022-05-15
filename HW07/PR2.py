"""Imagine that you have a customer who wants to order some food, a waiter and a chef.
Use command design pattern and classes of your choice to implement this logic.
The main operation will be ordering the food, the waiter will decide (depending on the order)
if the order should be cooked by the chef or is it something they already have pre-made and
should just be served to the client. """

from abc import ABC, abstractmethod


class Order(ABC):
    @abstractmethod
    def cook(self):
        pass


class SimpleOrder(Order):
    def __init__(self, order):
        self.order = order

    def cook(self):
        print(f"Serve precooked meal: {self.order}")


class ComplexOrder(Order):
    def __init__(self, receiver, meal_name):
        self._receiver = receiver
        self._meal_name = meal_name

    def cook(self):
        self._receiver.cook_special_meal(self._meal_name)


class Chef:
    def cook_special_meal(self, meal_name):
        print(f"Cooking only for you: {meal_name}")


class Client:
    _on_start = None
    _on_end = None

    def set_on_start(self, command):
        self._on_start = command

    def set_on_end(self, command):
        self._on_end = command

    def order_meal(self):
        if isinstance(self._on_start, Order):
            self._on_start.cook()

        if isinstance(self._on_end, Order):
            self._on_end.cook()


if __name__ == "__main__":
    client = Client()

    client.set_on_start(SimpleOrder("Jur"))
    chef = Chef()
    client.set_on_end(ComplexOrder(
        chef, "Horti jdbua"))

    client.order_meal()
