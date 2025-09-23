"""Create a class Person that takes name and age in its constructor.

Add a method introduce() that prints the string:

'My name is <name>, I am <age> years old.'"""


class Person:
    """create Person class"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f'Меня зовут {self.name}, мне {self.age} лет.')


print(Person.__doc__)
print(Person.__dict__)
print(dir(Person))
print(id(Person))

user = Person('Олег', 25)
user.introduce()