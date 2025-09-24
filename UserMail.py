class UserMail:
    logins = []
    def __init__(self, login, email):
        self.login = login
        self.email = email

    def get_login(self):
        return self._login

    def set_login(self, login):
        if not isinstance(login, str):
            raise TypeError(f"{login} не является строкой")
        elif login in UserMail.logins:
            raise ValueError(f"Логин {login} уже имеется в системе")
        else:
            self._login = login
            UserMail.logins.append(login)

    def get_email(self):
        return self._email

    def set_email(self, value):
        if isinstance(value, str) and value.count('@') == 1 and value[value.index('@'):].count('.') > 0:
            self._email = value
        else:
            print(f"ErrorMail:{value}")

    login = property(fget=get_login, fset=set_login)
    email = property(fget=get_email, fset=set_email)


jim = UserMail("aka47", 'hello@com.org')
print(isinstance(type(jim).login, property))
print(f'Jim login is {jim.login}')
try:
    bim = UserMail("aka47", 'world@com.org')
except ValueError as e:
    print(e)
jim.login = 'aka48'
print(f'Jim login is {jim.login}')
bim = UserMail("aka47", 'world@com.org')
print(f'Bim login is {bim.login}')
