class ShoppingCart:
    def __init__(self):
        self.items = {}

    def __getitem__(self, item):
        return self.items.get(item, 0)

    def __setitem__(self, item, total):
        self.items[item] = total

    def __delitem__(self, item):
        del self.items[item]

    def add_item(self, item, quantity=1):
        self.items[item] = self.items.setdefault(item, 0) + quantity

    def remove_item(self, item, quantity=1):
        if item in self.items:
            if self.items[item] > quantity:
                self.items[item] -= quantity
            else:
                del self.items[item]