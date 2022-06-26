winter_months = ['Dec', 'Jan', 'Oct', 'Feb', 'May', 'June']
print(type(winter_months) == list)
print(isinstance(winter_months, int))

nums = [1, 34, 25, 79, 1043]
print(dir(winter_months))
changes = ['EXTEND', 567, 'way']

nums.append(25)
print(nums)
nums.extend(changes)
print(nums)
print(nums.index(25))
nums.insert(8, 'INSERT')
print(nums)
look = nums.pop(7)
print(nums)
print(look)

new = nums[6: ]
print(new)
print(isinstance(nums, list)) # если тип эелемента верен, то True
print(nums[::-1]) # срез в обратном направлении
print(list(reversed(nums))) # то же самое, только с методом 'in place'
winter_months.sort() # in place возвращает None
print(winter_months)
winter_months.reverse() # in place возвращает None
print(winter_months)

cort = 'mask', 112, 'awesome', 'mask'
print(type(cort))
print(dir(cort))
print(cort.count('mask')) # какой индекс у элемента
print(cort.count(111))
m = 'sad'
print(ord(m[0])) # вызов номера элемента строки
print(chr(115)) # вызов элемента строки по номеру
print(chr(ord(m[1]) - 32)) # "-32" делает букву заглавной

raw_message = ['python', 'современный', 'язык']
message = ''
for item in raw_message:   # склеивание списка в строку
    message += item # new object!
    message += ' '
print(message)

message = ' '.join(raw_message) # склеивание списка в строку
print(message)

name, year, month, money = 'Борис', 2021, 3, 1789.47689

mes_2 = f'{name:^10}! Сегодня {month:02} месяц {year} года.'
mes_3 = f'{name:>10}! На счете {money:.2f}'

print(mes_2)
print(mes_3)

url = 'https://geekbrains.ru/teacher/lessons/79615'
_t_protocol, _, domain, *resource_address = url.split('/')
print(_t_protocol, domain, resource_address)

raw_url = ['https:', '', 'geekbrains.ru', 'teacher', 'lessons', '79615']
url = '/'.join(raw_url)
print(url)

print(message.upper())

msg = 'тОВАров в коРЗИНЕ: 5. стоимость: 4789,5 руб.'
print(msg.title())
print(msg.capitalize())
print(url[::-1])

new_word = ' '.join(raw_message)
print(new_word.capitalize())

nums = ['1578.4', '892.4', '354.1', '871.5']
print(sum(map(float, nums)))

print(map.__doc__)

def hello_print ():
    """Simple function, says hello,
    but you can modify me whenever you like!
    """
    name = input('Say your name! - ')
    print(f'Hello you charming {name}!')

print(help(hello_print))

def say_hello_wrapper():
    name = 'Петр'
    def say_hello():
        print(name)
    say_hello()
name = 'Иван'
say_hello_wrapper() # Петр





