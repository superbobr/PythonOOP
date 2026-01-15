class ReprMixin:
    def __repr__(self):
        attrs = ', '.join(f"{key}={value!r}" for key, value in self.__dict__.items())
        return f"{type(self).__name__}({attrs})"


class SomeClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class PrettyClass(SomeClass, ReprMixin):
    pass


class DictMixin:
    def to_dict(self):
        return {key: value
                for key, value in self.__dict__.items()
                if not key.startswith('_')}


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self._password_hash = None


class SerializableUser(DictMixin, User):
    pass