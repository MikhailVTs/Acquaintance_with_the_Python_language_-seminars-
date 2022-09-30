# Напишите программу для проверки истинности утверждения 

# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 

# для всех значений предикат.

print()
print("Введите значения: ")
print()

x = int(input(" 1. X = "))
y = int(input(" 2. Y = "))
z = int(input(" 3. Z = "))

result = (not (x or y or z)) == (not x and not y and not z)

print(result)