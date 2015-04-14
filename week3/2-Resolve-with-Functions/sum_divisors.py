#sum_divisors.py

def divisors(n):
    divisors_list = []

    counter = 1

    while counter < n:
        if n % counter == 0:
            divisors_list += [counter]

        counter += 1

    return divisors_list

def sum_divisors(numbers):
    result = 0

    for number in divisors(n):
        result += number

    return result

n = input("Enter number: ")
n = int(n)

# print(divisors(n))
# print(sum_divisors(n))
