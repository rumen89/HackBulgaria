# strings.py

# str_reverse:
# Същата функция, като reverse за списъци, само че обръща string наобратно:

def str_reverse(string):
    result = ""

    for ch in string:
        result = ch + result

    return result



# Една от най-полезните функциии, която ще използваме много, 
# когато боравим с низове в функцията join(delimiter, items)

def join(delimiter, items):
    result = ""

    for i in range(0, len(items) - 1):
        result += items[i] + delimiter

    result += items[len(items) - 1]

    return result



# Напишете функцията startswith(search, string), която проверява дали string, 
# започва с низа search.

def startswith(search, string):
    if search == take(len(search), string):
        return True

    return False


def take(n, items):
    result = ""

    for i in range(0 ,n):
        result += items[i]

    return result



# Напишете функцията endswith(search, string), която проверява дали string завършва с низа search.

def endswith(search, string):
    return startswith(str_reverse(search), str_reverse(string))




# Напишете полената функция trim(string), 
# която маха всички whitespace символи от началото и от края на string, 
# но запазва тези whitespace-ове вътре в самия string

def drop(n, string):
    result = ""

    for i in range(n, len(string)):
        result += string[i]

    return result


def white_spaces_count(string):
    count_white_spaces = 0

    for ch in string:
        if ch != " ":
            break

        count_white_spaces += 1

    return count_white_spaces

def trim(string):
    result = ""

    start = white_spaces_count(string)
    end = len(string) - white_spaces_count(str_reverse(string))

    for i in range(start, end):
        result += string[i]

    return result