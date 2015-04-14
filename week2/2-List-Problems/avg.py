#avg.py

n = input("Enter count of numbers: ")
n = int(n)

count = 1
numbers = []
sum_numbers = 0

while count <= n:
    number = input("Enter number: ")
    number = int(number)
    
    numbers = numbers + [number]

    count += 1

for number in numbers:
    sum_numbers += number

avg = sum_numbers / n

print("Avg is: " + str(avg))
