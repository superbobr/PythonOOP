class ConstantDescriptor:
    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        raise AttributeError("You cannot change a constant value.")


class MyClass:
    PI = ConstantDescriptor(3.14159)


class ManagedAttribute:
    def __set_name__(self, owner, name):
        self.private_name = '_' + name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.private_name, None)

    def __set__(self, instance, value):
        setattr(instance, self.private_name, value)


class ValidatedString:
    def __set_name__(self, owner, name):
        self.private_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.private_name, None)

    def __set__(self, instance, value):
        if isinstance(value, str):
            setattr(instance, self.private_name, value)
        else:
            raise TypeError()


class NonNegative:
    def __set_name__(self, owner, name):
        self.private_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.private_name)

    def __set__(self, instance, value):
        if isinstance(value, (int, float)) and value >= 0:
            setattr(instance, self.private_name, value)
        else:
            raise ValueError()


class LoggedAccess:
    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = '_' + name

    def __get__(self, instance, owner):
        print(f"Чтение атрибута '{self.public_name}'")
        return getattr(instance, self.private_name, None)

    def __set__(self, instance, value):
        print(f"Запись атрибута '{self.public_name}', новое значение = {value}")
        setattr(instance, self.private_name, value)