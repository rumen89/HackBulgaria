# beers_and_fries.py

# Мария държи известна бирария в София.

# Мария е създала интересна формула, с която може да оцени ефекта на всяка бира или 
# пък пържени картофи с дадена оценка - цяло число.

# Когато човек си поръча дадена бира с дадени пържени картофи, 
# общият ефект представлява произведението на оценката на бирата и пържените картофи.

# Например, ако имаме бира с оценка 10 и пържени картофи с оценка 5, 
# то общия ефект е 5 * 10 = 50

# Мария има следния казус - ако има списък с оценките на всички бири и списък с оценките 
# на всички пържени картофи (които по случайност са с равен брой), 
# то колко може да е максималната сума на комбиниран ефект между бира и пържени картофи?

# Във файл beers_and_fries.py, напишете функция max_score(beers, fries), която:

# Взима списък от цели числа beers, който представлява оценката на всяка бира.
# Взима списък от цели числа fries, който представлява оценката на всеки вид 
# пържени картофи.
# Списъците beers и fries винаги ще са с равна дължина!
# Функцията трябва да върне максималната оценка, получена от някаква комбинация между 
# beers и fries.

# Максималната оценка представлява сумата на всички оценки между бира и пържени картофи. 
# Само че трябва да е възможно най-голямата

def max_score(beers, fries):
    result = 0

    beers = sorted(beers)
    fries = sorted(fries)

    index = 0

    for beer in beers:
        result += beer * fries[index]

        index += 1

    return result

# print(max_score([1000, 1010, 1020, 1030, 1040], [834, 500, -1, 0, 60]))
# print(max_score([10, 11], [1, 5]))