import logging
from menu import Dish, MenuCategory, RestaurantMenu
from client import RegularDiscount, SilverDiscount, GoldDiscount, Client

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


"""Creating an approximate order"""
try:
    order = {"pizza": 10, "sandwich": 5, "beer": 15}
except SyntaxError:
    print("You filled out the order incorrectly")
    logging.exception(SyntaxError)


"""Creating customer categories"""
try:
    regular_client = Client("Jon", RegularDiscount())
    silver_client = Client("Maria", SilverDiscount())
    gold_client = Client("Sam", GoldDiscount())

    logger.info("The {RegularDiscount()} has been applied")
    logger.info("The {SilverDiscount()} has been applied")
    logger.info("The {GoldDiscount()} has been applied")

except TypeError:
    print("You did not specify the type of discount or name")
    logging.exception(TypeError)


try:
    print(f"If you are a regular client, amount to pay: {regular_client.get_total_price(order): .2f} UAH")
    print(f"If you are a silver client, amount to pay: {silver_client.get_total_price(order): .2f} UAH")
    print(f"If you are a gold client, amount to pay: {gold_client.get_total_price(order): .2f} UAH")
except NameError:
    print("Missing element")
    logging.exception(NameError)

try:
    dish1 = Dish("Caesar Salad", "Fresh romaine lettuce with Caesar dressing", 12.99)
    dish2 = Dish("Spaghetti Bolognese", "Spaghetti with meat sauce", 15.99)
    dish3 = Dish("Cheesecake", "Creamy cheesecake with raspberry sauce", 7.99)
except NameError:
    print("You entered incorrect value")
except TypeError:
    print("Missing positional argument")
    logger.exception(MoneyError)

try:
    appetizers = MenuCategory("Appetizers")
    appetizers.add_dish(dish1)

    main_courses = MenuCategory("Main Courses")
    main_courses.add_dish(dish2)

    desserts = MenuCategory("Desserts")
    desserts.add_dish(dish3)

    menu = RestaurantMenu()
    menu.add_category(appetizers)
    menu.add_category(main_courses)
    menu.add_category(desserts)

    print(menu)
except NameError:
    print("You have not completely filled out tre category: dish")

logger.info("Menu categories are filled")