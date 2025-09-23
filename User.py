"""Create a class User that stores username and email.

Implement the regular constructor __init__(self, username, email).

Implement a @classmethod method from_string(cls, user_string) that accepts a string in the format "username,email" and
creates a new User object."""


class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    @classmethod
    def from_string(cls, user_string):
        username, email = user_string.split(',')
        return cls(username, email)


user_data = "alice,alice@example.com"
user = User.from_string(user_data)
print(user.username, user.email)