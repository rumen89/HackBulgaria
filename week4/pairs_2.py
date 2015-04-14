# pairs_2.py

# Във файл pairs.py, напишете функция count_zero_pairs(numbers), която:

# Взима списък от цели числа items
# Връща броя на всички двойки числа в items, чиято сума е равна на 0.
# Ако имаме двойка (a, b), чиято сума е равна на 0, то я пребройте само 1 път.
# Вземете предвид и двойките, които се образуват от един и същи елемент в списъка, 
# но ги преброете 1 път
# Ако имаме numbers = [0, 2, -2, 5, 10], то двойките, чиято сума е равна на 0 са:

# 0, 0
# 2, -2
# С обща бройка 2.

def count_zero_pairs(numbers):
    result = 0

    for x in range(0, len(numbers)):
        for y in range(x, len(numbers)):
            i = numbers[x]
            j = numbers[y]

            if i + j == 0:
                result += 1

    return result

# numbers = [0, 2, -2, 5, 10, -10, -5, 0]

# print(count_zero_pairs(numbers))