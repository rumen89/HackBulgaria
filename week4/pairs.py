#pairs.py

# Във файл pairs.py, напишете функция count_zero_neighbours(numbers), 
# която:

# Взима един списък с цели числа numbers
# Връща броя на съседните числа в този списък, чиято сума е равна на 0.
# Ако преброите две числа с индекси Ai, Aj, където j = i + 1, 
# не бройте същата двойка наобратно - Aj, Ai.
# Например, ако имаме:

# numbers = [1, 2, -2, 0, 0, 5, -5], 
# то общата бройка е 3 - 2, -2, 0, 0, 5, -5

def count_zero_neighbours(numbers):
    n = len(numbers)

    count = 0

    for index in range(0, n):
        if index < len(numbers) - 1:
            neighbour = numbers[index + 1]

        if numbers[index] + neighbour == 0:
            count += 1

    return count

# print(count_zero_neighbours([1, 2, -2, 0, 0, 5, -5]))