# Напишите программу, которая принимает на вход 
# вещественное число и показывает сумму его цифр

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

print()
number = float(input("Введите вещественное число: "))
print()
sumNum = 0

for i in str(number):
    if i == ".":
        continue
    else:
        sumNum +=int(i)
print(f"- {number} -> {sumNum}")
print()