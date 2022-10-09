# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

import random

text_1 = 'text_1.txt'
text_2 = 'text_2.txt'
text_3 = 'text_3.txt'

k = int(input("Введите коэффициент, коэффицент должен быть k > 0: "))

with open(text_1, 'a', encoding='utf-8') as file:
    for elem in reversed(range(1, k +1)):
        number = random.randint(0, 100)
        if number != 0:
            print(f"{number} * x ^ {elem} + ", file = file, end = ' ')
    else:
        print(f"{number} = 0", file = file)

k = int(input("Введите коэффициент, коэффицент должен быть k > 0: "))

with open(text_2, 'a', encoding='utf-8') as file:
    for elem in reversed(range(1, k +1)):
        number = random.randint(0, 100)
        if number != 0:
            print(f"{number} * x ^ {elem} + ", file = file, end = ' ')
    else:
        print(f"{number} = 0", file = file)

with open(text_1, 'r', encoding='utf-8') as file:
    text_1 = file.read()

with open(text_2, 'r', encoding='utf-8') as file:
    text_2 = file.read()

with open(text_3, 'w', encoding='utf-8') as file:
    file.write(text_1 + text_2)