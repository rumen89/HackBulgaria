#first_n_perfect.py

n = input("Enter number: ")
n = int(n)

number = 6

print("Perfect numbers are: ")
while True:
    
    divisors_sum = 0
    counter = 1
    
    while counter < number:
        if number % counter == 0:
            divisors_sum += counter
        counter += 1
#        print(divisors_sum)

    

    if divisors_sum == number:
        n -= 1
        print(divisors_sum)

    if n == 0:
        break

    number += 1
