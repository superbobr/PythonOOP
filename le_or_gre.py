import random


random.seed(int(input()))
secret_number = random.randint(1, 100)
user_number = None

while user_number != secret_number:
    user_number = int(input())
    if user_number < secret_number:
        print('Больше')
    elif user_number > secret_number:
        print('Меньше')
    else:
        print('Угадал!')
        break