# Задайте список из n чисел, заполненный по формуле 
# (1 + 1/n)**n и вывидите на экран их сумму.

# Пример:

# - n = 6: [2, 2, 2, 2, 2, 3] -> 13

from subprocess import list2cmdline

print()
number = int(input("Введите число: "))
print()

list=[]
for i in range(1, number+1):
    list.append(int(round(((1 + 1 / i)**i),0)))

print(f"- n = {number}: {list} -> {sum(list)}")
print()