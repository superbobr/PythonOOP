class SparseArray:
    def __init__(self, *items):
        self._items = {} or dict(enumerate(items))

    def __getitem__(self, item):
        if item < 0:
            raise IndexError("Индекс не может быть отрицательным")
        elif item >= len(self._items):
            temp = {i:None for i in range(len(self._items), item + 1)}
            self._items.update(temp)
        return self._items.get(item, None)

    def __setitem__(self, item, value):
        if item < 0:
            raise IndexError("Индекс не может быть отрицательным")
        elif item >= len(self._items):
            temp = {i:None for i in range(len(self._items), item + 1)}
            self._items.update(temp)
        self._items[item] = value

    def __delitem__(self, item):
        if item < 0:
            raise IndexError("Индекс не может быть отрицательным")
        elif 0 <= item < len(self._items):
            self._items[item] = None

    def __len__(self):
        return len(self._items)

    @property
    def values(self):
        return tuple(self._items.values())