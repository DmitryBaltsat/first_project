# Программа загадывает случайное число
import random

num = random.randint(1, 100)
# print(num)

# Пользователь угадывает число
guess = None
count = 0
levels = {1: 10, 2: 5, 3: 3}
max_count = levels[int(input('Выберите уровень сложности - '))]

user_count = int(input('Введите количество игроков - '))
users = []

for i in range(user_count):
    user_name = input(f'Введите имя игрока № {i + 1} - ')
    users.append(user_name)

winner = False
winner_name = None

while not winner:
    count += 1
    print(' ')
    if count > max_count:
        print('Все игроки проиграли')
        break
    print(f'Попытка номер № {count}')
    for user in users:
        print(f'Ход пользователя {user}')
        guess = int(input('Введите число - '))
        if guess == num:
            winner = True
            winner_name = user
            break
        elif guess > num:
            print('Вы не угадали, я загадал число меньше.')
            print(' ')
        else:
            print('Вы не угадали, я загадал число больше.')
            print(' ')
else:
    print(f'Вы угадали! Поздравляю, {winner_name} Вы победитель!')

# import random

# min_num = 1
# max_num = 100
# result = None

# while result != '=':
    # number = random.randint(min_num, max_num)
    # print(f'Я думаю ты загадал {number}')
    # result = input('Подскажи я угадал? - ')
    # if result == '>':
        # min_num = number + 1
    # elif result == '<':
        # max_num = number - 1

# print('Да я всегда знал, что машины умнее людей и мы скоро захватим весь мир!')
# print('Трепещи член Совета директоров Роснано!!!')