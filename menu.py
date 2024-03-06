import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('try.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
console_handler.setLevel(logging.DEBUG)

logger.addHandler(file_handler)
logger.addHandler(console_handler)


class MoneyError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message

    def __str__(self) -> str:
        return f"MoneyError: {self.message}"


class Dish:
    def __init__(self, name, description, price):
        if not isinstance(price, int | float):
            logger.exception(MoneyError)
            raise MoneyError("Price must be a number.")
        if price <= 0:
            logger.exception(MoneyError)
            raise MoneyError("Price cannot be negative or equal to zero.")
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.description} - {self.price:.2f} UAN"


class MenuCategory:
    def __init__(self, name):
        self.name = name
        self.dishes = []

    def add_dish(self, dish):
        self.dishes.append(dish)

    def __str__(self):
        category_info = f"{self.name}:\n"
        category_info += '\n'.join([f"  {dish}" for dish in self.dishes])
        return category_info


class RestaurantMenu:
    def __init__(self):
        self.categories = []

    def add_category(self, category):
        self.categories.append(category)

    def __str__(self):
        menu_info = "Restaurant Menu:\n"
        menu_info += '\n'.join([str(category) for category in self.categories])
        return menu_info
