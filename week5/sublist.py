# sublist.py
# Във файла sublist.py, напишете функцията sublist(list1, list2), 
# която проверява дали list1 е подсписък на list2.

# Казваме, че един списък е подсписък на друг, 
# ако всички негови елементи ги има като последователност в другия списък.

# Например списъкът [1, 2, 3] е подсписък на [0, 0, 1, 2, 3, 5, 6].
# Празният списък - [] - е подсписък на на всеки други списък.
# Функцията sublist трябва да върне True или False

def take(n, list):
    result = []

    for i in range(0, n):
        result += [list[i]]

    return result

def tail(list):
    result = []

    index = 1

    for i in range(index, len(list)):
        result += [list[i]]

    return result

def sublist(list1, list2):

    while True:
        if list1 == take(len(list1), list2):
            return True
        else:
            list2 = tail(list2)

        if len(list2) <= len(list1):
            break

    return False

# print(sublist([1, 2], [0, 1, 2, 3]))