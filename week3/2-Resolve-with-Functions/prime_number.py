#prime_number.py

def to_digit(n):
    result = []

    while n != 0:
        digit = n % 10

        result = [digit] + result

        n = n // 10

    return result

def is_prime(digits):
    index = "Да"
    index_2 = "Не"
    prime_digits = [2, 3, 5, 7]

    for digit in digits:
        if digit in prime_digits:
            return index

    return index_2

n = input("Enter some number: ")
n = int(n)

# print(to_digit(n))
# print(is_prime(to_digit(n)))
