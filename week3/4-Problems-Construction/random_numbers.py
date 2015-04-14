# random_numbers.py

# Във файл random_numbers.py, напишете функция 
# generate_random_list(n, start, end), която прави следното нещо:

# Генерира списък с n на брой елементи
# Всеки елемент е цяло число, което се намира в затворения интервал 
# [start, end]
# Например:

# >>> generate_random_list(5, 1, 3)
# [1, 2, 1, 3, 1]

from random import randint

def generate_random_list(n, start, end):
    counter = 1

    result = []

    while counter <= n:
        number = randint(start, end)

        result += [number]

        counter += 1

    return result

# print(generate_random_list(5, 1, 4))