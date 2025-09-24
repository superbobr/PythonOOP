"""Implement a UserProfile class that encapsulates user data. The class should:

Store:

a public attribute username,
a protected attribute _email,
a private attribute __password.
 Have the following methods:

check_password(password) — returns True if the provided password matches the current one,
change_password(old, new) — replaces the current password with a new one only if the provided old password matches the current one,
get_password() — returns the current password."""

class UserProfile:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.__password = password

    def get_password(self):
        return self.__password

    def check_password(self, password):
        if self.__password == password:
            return True

    def change_password(self, old, new):
        if self.check_password(old):
            self.__password = new







