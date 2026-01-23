from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


class DataSource(ABC):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data):
        pass


class FileStorage(DataSource):
    def read(self):
        return "Чтение из файла"

    def write(self, data):
        return f"Запись в файл: {data}"


class Instrument(ABC):
    def __init__(self, brand):
        self.brand = brand

    def show_brand(self):
        return f"Бренд: {self.brand}"

    @abstractmethod
    def play(self):
        pass


class Guitar(Instrument):
    def play(self):
        return "Играет мелодия на гитаре"