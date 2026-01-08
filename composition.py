class Brain:
    pass


class Person:
    def __init__(self, name):
        self.name = name
        self.brain = Brain()


class CPU:
    def calculate(self):
        return "Вычисления..."


class Computer:
    def __init__(self):
        self.cpu = CPU()

    def run(self):
        return self.cpu.calculate()


class Engine:
    def start(self):
        return "Двигатель запущен"


class Wheels:
    def rotate(self):
        return "Колеса вращаются"


class Car:
    def __init__(self):
        self.engine = Engine()
        self.wheels = Wheels()

    def drive(self):
        return f"{self.engine.start()} и {self.wheels.rotate()}"


