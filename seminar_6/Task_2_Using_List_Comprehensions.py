# using list comprehensions
# filter
# Lambda

list_number = [num for num in range(20, int(input("Введите число до какого значения необходимо найти данные: "))+1)]
new_list = list(filter(lambda i: (i % 20 == 0 or i % 21 == 0) , list_number))

print(new_list)