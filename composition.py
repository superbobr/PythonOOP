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


class Chapter:
    def __init__(self, title):
        self.title = title

    def get_title(self):
        return self.title


class Book:
    def __init__(self, title, chapters):
        self.title = title
        self.chapters = []
        for chapter in chapters:
            self.chapters.append(Chapter(chapter))

    def get_table_of_contents(self):
        temp = f"{self.title}\n"
        for i, j in enumerate(self.chapters, start=1):
            temp += f"Глава {i}: {j.title}\n"

        return temp.rstrip()