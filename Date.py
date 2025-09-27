"""Your task is to create a `Date` class that stores date information: day, month, and year.

The `Date` class must also have a factory method `from_str`, which takes a string in the format:

day-month-year

and returns a newly created instance of the `Date` class based on this string.

Analyze the test input data to understand the required attributes of the `Date` class.

For this task, you only need to implement the `Date` class itself."""


class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_str(cls, string):
        return cls(*map(int, string.split('-')))


day_1 = Date(20, 9, 1997)
print(day_1.day)
print(day_1.month)
print(day_1.year)

day_2 = Date(1, 2, 2003)
print(day_2.day, day_2.month, day_2.year)

day_1 = Date.from_str('12-4-2024')
day_2 = Date.from_str('06-09-2022')
print(day_1.day, day_1.month, day_1.year)
print(day_2.day, day_2.month, day_2.year)