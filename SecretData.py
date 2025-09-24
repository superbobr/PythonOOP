"""Create a SecretData class with a private attribute __secret. Add:

a @property getter named secret,
a @secret.deleter that prints the message "Элемент удалился..." and deletes the attribute."""


class SecretData:
    def __init__(self, secret):
        self.__secret = secret

    @property
    def secret(self):
        return self.__secret

    @secret.setter
    def secret(self, value):
        self.__secret = value

    @secret.deleter
    def secret(self):
        print('Элемент удалился')
        del self.__secret


data = SecretData(input())
del data.secret