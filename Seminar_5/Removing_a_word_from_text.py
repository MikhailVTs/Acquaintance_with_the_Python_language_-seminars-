# Напишите программу, удаляющую из текста все слова, содержащие "абв".
# В тексте используется разделитель пробел.

import random

def random_word():
    for word in range(10):
        list_word.append(''.join([random.choice(combination_of_letters) for letter in range(3)]))
    print(list_word)

def del_word():
    for word in list_word:
        if combination_of_letters != word:
            new_list_word.append(word)
    print(new_list_word)

def main():
    random_word()
    del_word()

combination_of_letters = "абв"

list_word = []
new_list_word = []

if __name__ == '__main__':
    main()
