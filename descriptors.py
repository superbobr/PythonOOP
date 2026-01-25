class ConstantDescriptor:
    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        raise AttributeError("Cannot change a constant value. PI is read-only.")


class MyClass:
    PI = ConstantDescriptor(3.14159)


