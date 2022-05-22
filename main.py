# Урок 1 - часть первая.

print('У нас всего 10 яблок')

print(3==3)
print(3>=2)
print(6!=10)

apples_eaten = float(input('Сколько яблок ты съела?'))
apple_left = int(((apples_eaten - 10)  / 10 * 100) * -1)
print('Осталось', str(apple_left) + '%', 'яблок.')

age = int(input('Введите свой возраст - '))
goal_age = (2**4)
if age < goal_age:
    print('Доступ запрещен.')
elif age >= goal_age and age <= (goal_age + 2):
    print('Ограниченный доступ.')
else:
    print('Доступ разрещен.')
    if age % 10 == 0:
        print('Поздравляем у Вас юбилей!')

# Урок 1 - часть вторая.

number = 43
value = int(input('Введите число от 1 до 100 - '))

if value == number:
    print('Вы угадали число! Число равно -', str(number) + '.')

elif value >= (number - 5) and value <= (number + 5):
    print('Вы почти угадали, попробуйте еще раз.')
    if value < number:
        print('Нужно больше.')
    else:
        print('Нужно меньше.')

else:
    print('Вы не угадали число, повезет в другой раз.')
    if value < number:
        print('Нужно больше.')
    else:
        print('Нужно меньше.')

# Урок 1 - часть третья.

# инструкция break
name = None

while name != 'Гвидо':
        name = input('Кто создатель Python? - ')
        if name == 'Гвидо':
            break
        print('Неверно.')

print('Верно.')

while True:
        name = input('Кто похож на маленького фюрера? - ')
        if name == 'Зеленский':
            break
        print('Неверно.')

print('Верно.')

# инструкция continue
number = int(input('Введите число - '))
n = 0
while n <= number:
    if n % 2 == 0:
        n += 1
        continue
    print(n)
    n += 1

# инструкция while-else
n = 0
while n <= 30:
    print(n)
    n += 1
    # if n == 25:
        #break
else:
    print('else')

print('end')

# Урок 1 - часть четвертая.

name = input('Please enter your name - ')
age = int(input('Please enter your age - '))
weight = int(input('Please enter your weight - '))


if age <= 30 and (weight >= 50 and weight <= 120):
    print("I'm", name, age, "years old and I'm in good condition.")
elif (age > 30 and age < 40) and (weight < 50 or weight > 120):
    print("I'm", name, age, "years old and I need to take care of myselfe.")
elif age >= 40 and (weight < 50 or weight > 120):
    print("I'm", name, age, "years old and I need medical care.")
elif age < 40 and (weight >= 50 and weight <= 120):
    print("I'm", name, age, "years old and I need to do sports and visit gym.")

# Урок 2 - часть первая.

friends = 'Sandy,Tesla,1,3'
print(friends)
print(len(friends))
print(friends.find('T'))
print(friends.split(','))
print(friends.isdigit())
print(friends.upper())
print(friends.lower())

numbers = '123'
print(numbers.isdigit())

# Урок 2 - часть вторая.

glue_str = 'Привет, я ' + name + ' и мне ' + str(age) + ' лет'
print(glue_str)

glue_str = 'Привет, я %s и мне %d лет'%(name,age)
print(glue_str)

glue_str = 'Привет, я {} и мне {} лет'.format(name, age)
print(glue_str)

competition = 'Первые 5 мест на соревнованиях: 1. иванов 2. петров 3. сидров 4. орлов 5.соколов'
start = competition.find('1')
end = competition.find('2')
top3 = competition[start + 3: end - 1]

print('Поздравляем {}А с успрехом!'.format(top3.upper()))

# Урок 2 - часть третяя.

print('Соревнонвания по Python!')
count = int(input('Сколько человек учавствовали в соревновании? - '))
i = count
members = []

while i > 0:
    name = input('Кто занял {} место? - '.format(i))
    members.append(name)
    i -= 1

print('В соревновании участвовали: {}'.format(sorted(members)))

winners = members.reverse()
winners = members[:3]

print('Победители: {}. Поздравляем!'.format(winners))


# Урок 2 - часть четвёртая.

friends = ['Max', 'Leo', 'Kate', 'Ann']
roles = ('admin', 'guest', 'user')

i = 0
while i < len(friends):
    name = friends[i]
    print(name)
    i += 1

for role in roles:
    print(role)

name = input('Как Вас зовут? - ')
weight = float(input('Введите Вашу массу тела в кг. - '))
height = float(input('Введите Ваш рост в формате #.## - '))

imt = weight / (height**2)

if imt < 25:
    print(name + ', поздравляем Ваш вес в пределах нормы!')

elif imt <= 25 and imt <= 29.9:
    print(name + ', у Вас избыточный вес, нужно больше двигаться!')

elif imt <= 30 and imt <= 34.9:
    print(name + ', у Вас I степень ожирения, нужно больше двигаться и правильно питаться!')

elif imt <= 35 and imt <= 39.9:
    print(name + ', у Вас II степень ожирения, нужно заниматься собой и обратиться за консультацией к врачу!')

else:
    print(name + ', срочно обратитесь за помощью к профильному специалисту!!!')

# Урок 2 - часть пятая.

winners = ['Max', 'Kate', 'Ann', 'Leo']

for i in range(len(winners)):
    print(i + 1, ' - ', winners[i])

print(list(range(0, 20, 2)))

nums = range(0, 21, 2)
for num in nums:
    print(num)

# Урок 2 - часть шестая.

friend = {
    'name': 'Max',
    'age': 39,
    'sex': 'Male'
}

print(friend['name'])
print(type(friend['name']))
friend['height'] = 184
del friend['sex']
print(friend)
if 'age' in friend:
    print('Возраст есть')
print(' ')

# перебор по ключам
for key in friend.keys():
    print(key)
# for key in friend:
    # print(key)

# перебор по значениям
for val in friend.values():
    print(val)

# перебор пара ключ: значение
for item in friend.items():
    print(item)

for key, val in friend.items():
    print(key, '-', val)

# Урок 2 - часть седьмая.

cities = {'Moscow', 'Athens', 'Minsk', 'Kazan', 'Tokyo'}
cities.add('Beijing')
cities.remove('Athens')
print(len(cities))
print('Minsk' in cities)
for city in cities:
    print(city)

# работа с несколькими множествами
max_things = {'Telephone', 'Toothstick', 'Shorts', 'Shirt'}
kate_things = {'Telephone', 'Shorts', 'Umbrella', 'Lipstick'}
# объединение
print(max_things | kate_things)
# поиск повторений
print(max_things & kate_things)
# поиск разногласий
print(max_things - kate_things)
print(kate_things - max_things)

# Урок 2 - домашнее задание.

# Задача №1

my_list_1 = [1, 1, 1, 2, 2, 2, 3, 4, 4, 5]
my_list_2 = [2, 4, 5]

for num in my_list_1[:]:
    if num in my_list_2:
        my_list_1.remove(num)
print(my_list_1)

# Задача №2

date = input('Введите дату в формате дд.мм.гггг - ')
d, m, y = date.split('.')

date_dict = {
    '01': 'первое',
    '02': 'второе',
    '03': 'третье',
    '04': 'четвертое',
    '05': 'пятое',
}

months_dict = {
    '01': 'января',
    '02': 'февраля',
    '03': 'марта',
    '04': 'апреля',
    '05': 'мая'
    }
result = f'{date_dict[d]} {months_dict[m]} {y} года.'
print(result)

# Задача №3

numbers = [1, 1, 2, 3, 3, 4, 4, 4, 5, 1, 2, 7]
unique = []
for number in numbers:
    if numbers.count(number) == 1:
        unique.append(number)
print(unique)

# Урок 3 - часть первая.

num = range(23, 34)
num2 = {1, 2, 15, 28.2568, 2}

for number in num2:
    new_num = round(number)
    print(new_num)

player = ['Kate', 'Leo', 'Max']
# new_player = enumerate(player, 1)

for number, player in enumerate(player, 1):
    print(number, player)

print(round(sum(num2)))

numbers = []
count = int(input('Введите длину библиотеки - '))
while len(numbers) < count:
    number = int(input('Введите число - '))
    numbers.append(number)
min_num = min(numbers)
max_num = max(numbers)
sum_num = sum(numbers)
mid_num = sum_num / len(numbers)
print('Перечень -', *numbers, sep=' ')
print(' - - - ')
print(f'Минимальное число выборки - {min_num}, максимальное число {max_num}, среднее значение {mid_num}, а сумма равна {sum_num}.')

# Урок 3 - часть вторая.

def sq_area(amount):
    len = int(input('Введите длину - '))
    width = int(input('Введите ширину - '))
    area = len * width
    total_area = amount * area
    return total_area

print(f'Площадь равна {sq_area(2)} метра.')

# Урок 3 - часть третья.

def hello(name, type='Hello!'):
    print(f'Whazzupp! {type} {name}!')


# hello(name=input('Your name please - '), type=input('Greeting please - '))


def hello_1(*name, type='Hello!'):
    print(f'Whazzupp! {type} {name}!')


hello_1('Boris', 'Max', 'Leo')

def get_person(**petrol):
    for k, w in petrol.items():
        print(k, w)

get_person(name='- Edward', greetings='- Hi', bold='- Yes')

# Урок 3 - часть четвертая.

def num():
    return 'Something'
result = num()
print(result)

def a():
    print('Or not something')
def b(shit):
    shit()
b(a)

# филтрация чисел
def my_filter(numbers, function):
    result = []
    for num in numbers:
        if function(num):
            result.append(num)
    return result

numbers = [1, 2, 3, 4, 5, 7, 6, 8, 9, 10]

print(my_filter(numbers, lambda num: num % 2 == 0))
print(my_filter(numbers, lambda num: num % 2 != 0))

print(sorted(numbers))
print(sorted(numbers, reverse=True))

cities = [('Moscow', 1000), ('Minsk', 500), ('Athens', 700)]

# def by_count(city):
    # return city[1]

print(sorted(cities, key=lambda city: city[1] , reverse=True))

def is_even(num):
    return num % 2 == 0

def not_even(num):
    return num % 2 != 0

print(list(filter(not_even, numbers)))
print(list(filter(is_even, numbers)))

names = 'Max', 'Leo', 'Kate', 'Ivan'
print(list(filter(lambda x: len(x) > 3, names)))

other_numbers = [5, 3, 4, 7, 8]
# получить список квадратов чисел
print(list(map(lambda x: x**2, other_numbers)))
# привести числа к строке
print(list(map(lambda x: str(x), other_numbers)))

# Урок 3 - домашнее задание.

# Задача № 1
def people_data(name, age, city):
    return f'{name}, {age} лет(год/а), проживает в городе {city}.'

print(people_data('Дмитрий','39','Москва'))

# Задача № 2
def count_num(num1, num2, num3):
   number = max(num1, num2, num3)
   return number

print(count_num(16578, 2034, 654))

# Задача № 3, 4

player = {'name': input('Введите имя игрока - '), 'health': 100, 'damage': 100, 'armor': 1.7}
enemy = {'name': input('Введите имя противника - '), 'health': 300, 'damage': 50, 'armor': 1}

def armor_block(damage, armor):
    return damage / armor

def attack(attacker, defender):
    damage = armor_block(attacker['damage'], defender['armor'])
    defender['health'] -= damage

attack(player, enemy)
attack(enemy, player)
p_health = round(player['health'])
p_name = player['name']
e_health = round(enemy['health'])
e_name = enemy['name']
print(f'У {p_name} осталось {p_health} жизней.')
print(f'У {e_name} осталось {e_health} жизней.')

# Урок 4 - модуль (библиотека) math.

# print(math.pi)
# print(math.sin(38))

# from random import randint, randrange
# print(randint(1, 10))
# for i in range(2, 8):
    # print(i)

import math

# найти длину окружности
r = 100
print(2*r*math.pi)

# найти площадь окружности
print((r**2)*math.pi)
print((math.pow(r, 2)*math.pi))

# по координатам двух точек определить расстояние между ними
x1 = 10
y1 = 10
x2 = 50
y2 = 100
dist = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
print((dist))

# найти факториал числа 9
print(math.factorial(9))

# Урок 4 - модуль (библиотека) random.

import random

# загадать случайное число
print(random.randint(1, 100))

# выбрать случайного победителя из списка
names = ['Max', 'Ann', 'Tom', 'Ivan', 'Kate', 'Daniel']
print(random.choice(names))

# выбрать 3 случайных победителей из списка
print(random.sample(names, 3))

# перемешать цифры в списке
numbers = [1, 23, 76, 104, 5, 29, 91]

random.shuffle(numbers)
print(numbers[1])

# Урок 4 - создание собственных модулей

