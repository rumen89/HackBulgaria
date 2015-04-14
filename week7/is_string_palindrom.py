# is_string_palindrom.py

# Във файл is_string_palindrom.py напишете функция is_string_palindrom(string) , 
# която приема стринг като аргумент и проверява дали той е палиндром, 
# връщайки True или False.

# Нещо е палиндром ако прочетено от ляво на дясно и прочетено от дясно на ляво е едно и също.

# Пример: "капак" от ляво на дясно е "капак", а от дясно на ляво... отново е "капак" :)
# Стрингът може дори да е цяло изречение с празни разстояния между думите или 
# стринг със шпации в него. Празните разстояния не пречат на палиндромността му
# В низа може да има и следните препинателни знаци: ",", ".", "!" и "?". 
# Те не пречат на палиндромността на низа!
# Не се интересуваме дали буквите са главни или малки. Програмата ни трябва да ги уеднакви.
# Примери:

# is_string_palindrom("Az obi4am ma4 i boza") --> трябва да върне True
# is_string_palindrom("A Toyota!") --> трябва да върне True
# is_string_palindrom("bozaaa") --> трябва да върне False
# is_string_palindrom(" kapak! ") --> трябва да върне True

def is_string_palindrom(string):
    result = ""
    new_string = ""

    removable_marks = [",", ".", "!", "?", " "]

    for ch in string:
        if ch not in removable_marks:
            new_string += ch

    for ch in new_string:
        result = ch + result

    if result == new_string:
        return True

    return False

# print(is_string_palindrom("  kapak!"))