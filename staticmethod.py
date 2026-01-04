class Formatter:
    @staticmethod
    def format_email(email):
        return email.lower().strip()


class Validator:
    @staticmethod
    def is_positive(number):
        return number > 0

    @staticmethod
    def is_even(number):
        return not (number % 2)


class Circle:
    def __init__(self, radius):
        if Circle._is_valid_radius(radius):
            self.radius = radius
        else:
            raise ValueError("Некорректный радиус")

    @staticmethod
    def _is_valid_radius(radius):
        if isinstance(radius, int) and radius > 0:
            return True
        return False


class Counter:
    total_count = 0

    def __init__(self):
        self.instance_count = 0
        Counter.total_count += 1

    def increment(self):
        self.instance_count += 1

    @classmethod
    def get_total_count(cls):
        return cls.total_count

    @staticmethod
    def get_description():
        return "Это класс для подсчета."