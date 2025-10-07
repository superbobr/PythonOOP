"""Editing the Vector class

Below is the implementation of the Vector class from the lesson. In this implementation, we use standard Python collection indexing, where the first element has index 0, followed sequentially.

Modify the code so that indexing starts from 1 instead of 0."""


class Vector:
    def __init__(self, *args):
        self.values = list(args)

    def __repr__(self):
        return f'Vector({", ".join([str(value) for value in self.values])})'

    def __getitem__(self, item):
        if 1 <= item < len(self.values) + 1:
            return self.values[item - 1]
        else:
            raise IndexError(f"Индекс {item} находится за пределами вектора")