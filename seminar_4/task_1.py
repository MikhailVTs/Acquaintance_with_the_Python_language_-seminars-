# from this import d


# Вычислить число с заданной точностью d

# Пример:

# - при d = 0.001, pi = 3.141

import math

pi = math.pi
d = float(input("Введите значение с точностью d: "))
# print(len(str(d)[2:]))
print(d)
if d >= 0.1 and d <= 0.0001:
    print(f"{pi:.{len(str(d)[2:])}f}")
if d >= 0.00001 and d <= 0.000000001:
    print(f"{pi:.{len(str(d)[4:])}f}")
if d >= 0.0000000001 and d <= 0.000000000000001:
    print(f"{pi:.{len(str(d)[3:])}f}")
