# Напишите программу, которая принимает на вход число N
# и выдаёт набор произведений чисел от 1 до N

# Пример:

# - пусть N = 4, тогда [1, 2, 6, 24] (1, 1*2, 1*2*3, 1*2*3*4)

print()
number = int(input("Введите число: "))
print()

list = []

for i in range(2, number+1):
    numbers = 1
    for j in range(1, i):
        numbers *= j
    list.append(numbers)

print(f"- пусть N = {number}, тогда {list}")
print()