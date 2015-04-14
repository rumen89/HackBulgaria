#surname.py

# Във файл surname.py напишете функция taken_name(surname_husband,
# surname_wife), която:

# приема два аргумента - фамилията на мъжа и фамилията на жената.
# функцията връща True, ако жената е взела фамилията на мъжа и False, 
#ако не е.

def taken_name(surname_husband, surname_wife):
    index = 0

    if surname_husband in surname_wife:
        return True

    return False

# print(taken_name("tsvetkov", "tsvetkova"))