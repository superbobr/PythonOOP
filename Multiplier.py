"""Create a Multiplier class that stores a number.
When an instance is called as a function—e.g., obj(x)—it should return x * number."""


class Multiplier:
    def __init__(self, number):
        self.number = int(number)

    def __call__(self, mult):
        return self.number * int(mult)


new_multiplier = Multiplier(input())
print(new_multiplier(input()))