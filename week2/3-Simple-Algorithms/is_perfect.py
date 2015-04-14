#is_perfect.py

n = input("Enter number: ")
n = int(n)

count = 1
sum_divisors = 0
divisors = []

while count < n:
    if n % count == 0:
        divisors += [count]
    count += 1

for number in divisors:
    sum_divisors += number

if n == sum_divisors:
    print("The number is perfect")
