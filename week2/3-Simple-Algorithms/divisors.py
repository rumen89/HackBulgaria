#divisors.py

n = input("Enter number: ")
n = int(n)

count = 1

while count < n:
    if n % count == 0:
        print(count)
    count += 1
