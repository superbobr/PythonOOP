import random


random.seed(int(input()))
game = ('камень', 'ножницы', 'бумага')
user_input = input()
pc_input = random.choice(game)

if user_input == pc_input:
    print('Ничья.')
elif user_input == 'камень' and pc_input == 'ножницы':
    print('Победа!')
elif user_input == 'ножницы' and pc_input == 'бумага':
    print('Победа!')
elif user_input == 'бумага' and pc_input == 'камень':
    print('Победа!')
else:
    print('Поражение!')