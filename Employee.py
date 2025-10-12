class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        return self.salary

class Developer(Employee):
    def calculate_salary(self):
        return super().calculate_salary() * 1.2

class Manager(Employee):
    def calculate_salary(self):
        return super().calculate_salary() * 1.3

class TechLead(Developer, Manager):
    def calculate_salary(self):
        base_with_bonuses = super().calculate_salary()
        extra_bonus = self.salary * 0.2
        return base_with_bonuses + extra_bonus