"""Create a payroll calculation system for employees:
A base class Employee with a method get_salary() that returns the base rate.
A class HourlyEmployee that overrides get_salary() to return hours * rate.
A class SalariedEmployee that returns a fixed salary.
A class Manager that inherits from SalariedEmployee but adds a bonus: super().get_salary() + bonus.
A function print_report(employees: list) that calls get_salary() for each employee object and prints:
Employee: <name>, Salary: <amount>
"""


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        return self.salary

class HourlyEmployee(Employee):
    def __init__(self, name, salary, hours):
       super().__init__(name, salary)
       self.hours = hours

    def get_salary(self):
        return self.salary * self.hours

class SalariedEmployee(Employee):
    def __init__(self, name, salary, hours):
        super().__init__(name, salary)
        self.hours = hours

    def get_salary(self):
        return self.salary

class Manager(SalariedEmployee):
    def __init__(self, name, salary, hours, bonus):
        super().__init__(name, salary, hours)
        self.hours = hours
        self.bonus = bonus

    def get_salary(self):
        return super().get_salary() + self.bonus


def print_report(employees: list):
    for employee in employees:
        print(f'Сотрудник: {employee.name}, зарплата: {employee.get_salary()}')