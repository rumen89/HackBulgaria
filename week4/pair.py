# Във файла pair.py, напишете функция prime_pair(numbers), която:

# Взима един списък от цели числа numbers.
# Връща True, ако поне една произволна двойка числа от списъка, дава сума, 
# която е просто число.
# Вземете всички двойки предвид - дори и тези, които са съставени от 1 елемент, 
# участващ 2 пъти в двойката.

def is_prime(n):
    if n == 1:
        return False

    counter = 2

    while counter < n:
        if n % counter == 0:
            return False

        counter += 1

    return True

def prime_pair(numbers):
    for x in numbers:
        for y in numbers:

            if is_prime(x + y):
                return True

    return False

numbers = [6, 5, 6, 8, 21]

# print(prime_pair(numbers))