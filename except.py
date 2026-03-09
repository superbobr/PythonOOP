class InvalidAgeError(ValueError):
    pass


class Person:
    def __init__(self, name, age):
        if age < 0:
            raise InvalidAgeError("Возраст не может быть отрицательным")
        else:
            self.name = name
            self.age = age


try:
    number = int(input())
    print(number)
except ValueError:
    print("Ошибка: введено не число.")

try:
    print(int(input()) / int(input()))
except ZeroDivisionError:
    print("Ошибка: деление на ноль.")

my_list = [10, 20, 30]

try:
    print(my_list[int(input())])
except IndexError:
    print("Ошибка: неверный индекс.")

my_dict = {"a": 1, "b": 2}

try:
    print(my_dict[input()])
except KeyError:
    print("Ошибка: такого ключа нет.")

try:
    print(int(input()) / int(input()))
except (ValueError, ZeroDivisionError):
    print("Произошла ошибка ввода.")

try:
    num = int(input())
except ValueError:
    print("Ошибка ввода")
else:
    print("Преобразование успешно")

try:
    x = int(input())
    y = int(input())
    print(x / y)
except (ValueError, ZeroDivisionError) as e:
    print(f"Произошла ошибка: {type(e).__name__}")
finally:
    print("Завершение программы")

my_list = [0, 1, 2]

try:
    index = int(input())
    print(my_list[index])
except ValueError:
    print('Ошибка: индекс должен быть числом.')
except IndexError:
    print('Ошибка: такого индекса нет.')

while True:
    try:
        num = int(input())
    except ValueError:
        print("Неверный ввод, попробуйте снова")
    else:
        print("Спасибо!")
        break

with open("test.txt", "w", encoding="utf-8") as f:
    f.write('Это тестовый файл.')
try:
    file_name = input()
    with open(file_name, "r+", encoding="utf-8") as file:
              data = file.read()
              print(data)
except FileNotFoundError:
              print("Ошибка: файл не найден.")

