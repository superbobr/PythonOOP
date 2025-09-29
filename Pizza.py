"""Pizza
Now the pizzeria wants to implement a nice string representation for the Pizza and Ingredient classes.
The string representation of the Ingredient class should consist of the ingredient's name and its amount in grams.
The string representation of the Pizza class should start with the phrase:
Pizza <pizza_name> consists of:
followed by each ingredient listed on a separate line, ordered by descending amount (in grams).
"""


class Ingredient:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f'{self.name}: {self.weight}г.'

    def __repr__(self):
        return f'{self.name}: {self.weight}'


class Pizza:
    def __init__(self, name, ingredients=None):
        self.name = name
        if ingredients is None:
            self.ingredients = []
        else:
            self.ingredients = ingredients

    @staticmethod
    def ingredient_to_txt(ingredients):
        result = ''
        for ingredient in sorted(ingredients, key=lambda x: -x.weight):
            result += str(ingredient) + '\n'
        return result

    def __str__(self):
        return f'Пицца {self.name} состоит из:\n{self.ingredient_to_txt(self.ingredients)}'