"""Ask the user to input two numbers, `a` and `b`. Perform the division: `a / b`.
Handle the following exceptions:
- `ValueError` if the user enters non-numeric data. (Error: invalid input)
- `ZeroDivisionError` if `b == 0`. (Error: division by zero)
If no exceptions occur, print the result in the `else` block.
Regardless of whether an exception occurred or not, print "Operation completed" in the `finally` block."""

try:
    a = int(input())
    b = int(input())
    result = a / b
except ValueError:
    print('Ошибка: введены некорректные данные')
except ZeroDivisionError:
    print('Ошибка: деление на ноль')
else:
    print(f' Результат: {result}')
finally:
    print('Операция завершена')


#ApiError

class ApiError(Exception):
    pass


class AuthError(ApiError):
    pass


class TimeOutError(ApiError):
    pass


def make_request(should_fail_with: str):
    if should_fail_with == "auth":
        raise AuthError()
    elif should_fail_with == "timeout":
        raise TimeOutError()
    else:
        pass