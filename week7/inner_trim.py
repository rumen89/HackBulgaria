# inner_trim.py

# След като решихме проблема с премахване на празните пространства от началото и 
# края на даден низ, сега трябва да решим друг проблем - разстоянието между отделните думи, 
# ако то е по-голямо от 1 шпация.

# Във файл inner_trim.py напишете функция inner_trim(string), 
# която взима низ и прави 2 неща:

# trim-ва всички whitespace-ове от началото и края (това сме го решавали!)
# Нормализира всички разстояния вътре в string, до точно 1.

def tail(string):
    result = ""

    for i in range(1, len(string)):
        result += string[i]

    return result

def reverse(string):
    result = ""

    for ch in string:
        result = ch + result

    return result

def take(n, string):
    result = ""

    for i in range(0, n):
        result += string[i]

    return result

def drop(n, string):
    result = ""

    for i in range(n, len(string)):
        result += string[i]

    return result

def drop_start_spaces(string):
    counter = 0

    while string[counter] == " ":
        counter += 1

    return drop(counter, string)

def drop_end_spaces(string):
    string = reverse(string)

    return reverse(drop_start_spaces(string))

def inner_trim(string):
    result = ""

    string = drop_start_spaces(string)
#    string = drop_end_spaces(string)

    while True:
        while len(string) > 0 and string[0] != " ":
            result += string[0]

            string = tail(string)


        if len(string) == 0:
            break

        if len(string) > 1 and string[1] != " ":
            result += " "

        string = tail(string)

    return result

# print(inner_trim("   rumen     rumen   n"))