# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

import random

k = int(input("Введите коэффициент, коэффицент должен быть k > 0: "))

with open('text.txt', 'a', encoding='utf-8') as file:
    for elem in reversed(range(1, k +1)):
        number = random.randint(0, 100)
        if number != 0:
            print(f"{number} * x ^ {elem} + ", file = file, end = ' ')
    else:
        print(f"{number} = 0", file = file)

