"""You need to modify the implementation of the Vector class from the lesson once again. I've left it for you exactly as it appeared in the theory.

Now, implement the reverse behavior: when a value is provided as input (instead of an index), the method should return the position(s) of that value in the vector.

If the value appears multiple times, return a list containing all positions (indices) where this value occurs.
If the value is not present in the vector, raise a ValueError with the message: 'Value <value> is not in the vector'.
 Indexing must start from 1."""


class Vector:
    def __init__(self, *args):
        self.values = list(args)

    def __repr__(self):
        return f'Vector({", ".join([str(value) for value in self.values])})'

    def __getitem__(self, value):
        if value in self.values and self.values.count(value) == 1:
            return self.values.index(value) + 1
        elif self.values.count(value) > 1:
            temp = []
            for i, j in enumerate(self.values, start=1):
                if j == value:
                    temp.append(i)
            return temp
        else:
            raise ValueError(f'В векторе отсутствует значение {value}')