"""Create a TagList class that stores a list of strings (tags).
Implement the __contains__ method to allow using the in operator
for checking whether a string is present in the list of tags."""


class TagList:
    def __init__(self, *tags):
        if tags is None:
            self.tags = []
        else:
            self.tags = list(tags)

    def __contains__(self, item):
        if item in self.tags:
            return True
        return False