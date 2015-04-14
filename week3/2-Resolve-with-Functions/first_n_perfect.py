#first_n_perfect.py

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

    for number in numbers:
        result += number

    return result

def is_perfect(n):
    return sum_divisors(divisors(n)) == n

def first_n_perfect(n):
    start = 6

    perfect_numbers_list = []
    
    while n > 0:
        
        if is_perfect(start):
            n -= 1
            print(start)
            perfect_numbers_list += [start]

        start += 1

    return perfect_numbers_list


n = input("Enter number: ")
n = int(n)

# print(divisors(n))
# print(sum_divisors(divisors(n)))

if is_perfect(n):
    print(str(n) + " is perfect!")
else:
    print(str(n) + " is not perfect.")

# print(first_n_perfect(n))
