class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def area(self):
        return 3.14159 * self._radius ** 2


class Temperature:
    def __init__(self):
        self._celsius = 0

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, new_celsius):
        if new_celsius >= -273.15:
            self._celsius = new_celsius


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height


class Config:
    def __init__(self):
        self._port = 80

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, new_port):
        try:
            self._port = int(new_port)
        except ValueError:
            pass


class Converter:
    def __init__(self):
        self._meters = 0

    @property
    def meters(self):
        return self._meters

    @meters.setter
    def meters(self, new_value):
        self._meters = new_value

    @property
    def kilometers(self):
        return self._meters / 1000

    @kilometers.setter
    def kilometers(self, new_value):
        self._meters = new_value * 1000


