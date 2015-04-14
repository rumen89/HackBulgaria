#large_and_small.py

def digits(n):

    result = []

    while n != 0:
        digit = n % 10

        result = [digit] + result

        n = n // 10

    return result

def large_number(digits):
    result = 0

    large_number_list = sorted(digits, reverse = True)

    for digit in large_number_list:
        result = result * 10 + digit
    
    return result

def small_number(digits):
    result = 0

    small_number_list = sorted(digits)

    for digit in small_number_list:
        result = result * 10 + digit
    
    return result

n = input("Enter some number: ")
n = int(n)

# print(large_number(digits(n)))
# print(small_number(digits(n)))
