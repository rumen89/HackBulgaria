# list_functions.py

# Напишете функция head, която взима списък и връща първият елемент на този списък.
# Не се грижете, ако списъка е празен

def head(list):
    return list[0]

# print(head([1, 2, 3]))


# Напишете функция last, която взима списък и връща последния елемент на този списък
# Не се грижете, ако списъка е празен

def last(list):
    return list[len(list) - 1]

# print(last([1, 2, 3]))


# Напишете функция в Python, която взима списък и връща нов списък, 
# който се състои от всички елементи без първия от първоначалния списъка.
# Не се грижете, ако списъка е празен

def tail(list):
    n = 1

    result = []

    for item in range(n, len(list)):
        result += [list[item]]

    return result

# print(tail([1, 2, 3]))


# Напишете функция equal_lists, която взима два списъка и връща True, 
# ако двата списъка за еднакви.
# Казваме, че два списъка са еднакви, ако:
# Имат равна дължина
# Всеки елемент да индекс i в първия е равен (чрез ==) на елементът на индекс i във втория.

def equal_lists(list1, list2):
    if len(list1) != len(list2):
        return False

    n = 0

    for i in range(n, len(list1)):
        if list1[i] != list2[i]:
            return False

    return True

# print(equal_lists([1, 2], [1, 3]))


# Напишете функция count_item, която взима два аргумента - елемент и списък. 
# Функцията връща броят на срещанията на дадения елемент в дадения списък.

def count_item(n, list):
    result = 0

    for item in list:
        if item == n:
            result += 1

    return result

# print(count_item(1, [1, 2, 1, 4, 1, 1]))


# Напишете функция take, която взима два аргумента - цяло число и списък.
# Функцията връща нов списък, който се състои от първите n елемента, 
# където n е цялото число от първия аргумент.

def take(n ,list):
    result = []

    for i in range(0, n):
        result += [list[i]]

    return result

# print(take(3, [1, 2, 3, 4, 5, 5]))


# Напишете функция drop, която взима два аргумента - цяло число n и списък.
# Функцията връща нов списък, който представлява стария списък, без първите n елемента.

def drop(n, list):
    result = []

    for i in range(n, len(list)):
        result += [list[i]]

    return result

# print(drop(3, [1, 2, 3, 4, 5, 6]))


# Напишете функция reverse, която взима един списък и го връща обърнат. 
# Последния елемент става първи, предпоследния втори и т.н.

def reverse(list):
    result = []

    for item in list:
        result = [item] + result

    return result

# print(reverse([1, 2, 3]))