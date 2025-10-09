"""Add a __delitem__ method to the Vector class that removes all occurrences of the
iven value from the vector.
For example, if you have a vector
a = Vector(3, 4, 5, 5, 6, 6)
then the operation
del a[5]
should remove both elements whose value is 5.
If the given value is not present in the vector,
raise a ValueError with the message: 'Value <value> is not present in the vector'."""


class Vector:
    def __init__(self, *args):
        self.values = list(args)

    def __repr__(self):
        return f'Vector({", ".join([str(value) for value in self.values])})'

    def __getitem__(self, item):
        if 0 <= item < len(self.values):
            return self.values[item]
        else:
            raise IndexError(f"Индекс {item} находится за пределами вектора")

    def __delitem__(self, item):
        if item not in self.values:
            raise ValueError(f'Значение {item} отсутствует в векторе')
        else:
            while item in self.values:
                self.values.remove(item)