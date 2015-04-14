#is_prime.py

n = input("Enter number: ")
n = int(n)

counter = 2
index = True

if n == 1:
    index = False

while counter < n:
    if n % counter == 0:
        index = False
        break
    counter += 1

if index:
    print("The number is prime")
else:
    print("The number is not prime")

