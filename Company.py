"""Create a class Company with a class attribute company_name.

Implement the following methods:

@classmethod
def set_company(cls, name):
 Changes the value of company_name.

@classmethod
def get_company(cls):
 Returns the string: "My company is called - company_name"."""


class Company:
    company_name = None

    @classmethod
    def set_company(cls, name):
        cls.company_name = name

    @classmethod
    def get_company(cls):
        print(f'Моя компания называется - {cls.company_name}')

Company.set_company(input())
Company.get_company()