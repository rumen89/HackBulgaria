#divisors.py

def divisors(n):
    divisors_list = []

    counter = 1

    while counter < n:
        if n % counter == 0:
            divisors_list += [counter]

        counter += 1

    return divisors_list

n = input("Enter number: ")
n = int(n)

# print(divisors(n))
