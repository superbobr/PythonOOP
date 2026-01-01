class GameCharacter:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    @classmethod
    def create_default_character(cls):
        return cls("Guest", 1)


class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    @classmethod
    def from_string(cls, user_data_string):
        username, email = user_data_string.split(',')
        return cls(username, email)


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @classmethod
    def from_dict(cls, product_dict):
        name = product_dict.get('name')
        price = product_dict.get('price')
        return cls(name, price)


class Car:
    total_cars = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_cars += 1

    @classmethod
    def get_total_cars(cls):
        return cls.total_cars


