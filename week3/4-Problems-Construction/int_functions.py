#int_function.py

def reverse_int(x):
    reversed_number = 0

    while x != 0:
        number = x % 10

        reversed_number = reversed_number * 10 + number

        x = x // 10

    return reversed_number

def sum_digits(x):
    digit_sum = 0

    while x != 0:
        digit = x % 10
        
        digit_sum += digit

        x = x // 10

    return digit_sum

def product_digit(x):
    product = 1

    while x != 0:
        digit = x % 10

        product *= digit

        x = x // 10

    return product

# n = input("Enter number: ")
# n = int(n)

# print(reverse_int(n))
# print(sum_digits(n))
# print(product_digit(n))
