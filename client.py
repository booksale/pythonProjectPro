import logging

logger = logging.getLogger(__name__)


class Discount:
    """Creating the class Discount"""

    def discount(self):
        raise NotImplementedError


class RegularDiscount(Discount):
    """Creating the class RegularDiscount"""

    def discount(self):
        return 0.95


class SilverDiscount(Discount):
    """Creating the class SilverDiscount"""

    def discount(self):
        return 0.90


class GoldDiscount(Discount):
    """Creating the class GoldDiscount"""

    def discount(self):
        return 0.85


"""Creating the class Client with calculation the order amount"""


class Client:
    def __init__(self, name, discount):
        self.name = name
        self.discount = discount

    def get_total_price(self, order):
        total_price = sum(order.values())
        discount = self.discount.discount() * total_price
        return discount
