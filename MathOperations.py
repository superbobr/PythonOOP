"""Create a class MathOperations.

Add two static methods:

square(x): returns the square of the number x.
cube(x): returns the cube of the number x."""


class MathOperations:
    @staticmethod
    def square(number):
        return number ** 2

    @staticmethod
    def cube(number):
        return number ** 3



user_input = int(input())
print(MathOperations.square(user_input))
print(MathOperations.cube(user_input))