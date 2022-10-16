# Using List Comprehensions

# List comprehensions are a third way of making lists. 
# With this elegant approach, you could rewrite the for 
# loop from the first example in just a single line of code:

# -> squares = [i * i for i in range(10)]
# -> [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

import random


list_random_numbers = [random.randint(i, 50) for i in range(10)]
list_sort = [list_random_numbers[num] for num in range(1, len(list_random_numbers)) if list_random_numbers[num] > list_random_numbers[num -1]]

print(list_random_numbers)
print(list_sort)