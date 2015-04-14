#sum_divisors.py

n = input("Enter number: ")
n = int(n)

count = 1
sum_divisors = 0
divisors = []

while count < n:
    if n % count == 0:
        divisors = divisors + [count]
        print("Divisor is: " + str(count))
    count += 1

for number in divisors:
    sum_divisors += number

print("The sum divisors is: " + str(sum_divisors))
