class Point:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


class User:
    __slots__ = 'username'

    def __init__(self, username):
        self.username = username


class Base:
    __slots__ = ('x',)

    def __init__(self, x):
        self.x = x


class Child(Base):
    pass


class GameObject:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Player(GameObject):
    __slots__ = ('nickname',)

    def __init__(self, x, y, nickname):
        super().__init__(x, y)
        self.nickname = nickname


class FlexibleObject:
    __slots__ = ('fixed_attribute', '__dict__')

    def __init__(self, value):
        self.fixed_attribute = value