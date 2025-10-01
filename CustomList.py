"""Create a CustomList class that stores a list.
Add support for [] using the __getitem__ and __setitem__ methods."""


class CustomList:
    def __init__(self, *value):
        self.values = []
        self.values.extend(value)

    def __getitem__(self, item):
        if 0 <= item < len(self.values):
            return self.values[item]
        else:
            raise IndexError()

    def __setitem__(self, item, value):
        if 0 <= item < len(self.values):
            self.values[item] = value
        else:
            raise IndexError()


new_list = CustomList(input(), input(), input())
print(new_list[0])