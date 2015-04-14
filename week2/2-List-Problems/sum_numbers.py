#sum_numbers.py

n = input("Enter count of numbers: ")
n = int(n)

count = 1
numbers = []
sum_numbers = 0

while count <= n:
    number = input("Enter number: ")
    number = int(number)

    numbers = numbers + [number]

    sum_numbers = sum_numbers + number
    
    count += 1

print(numbers)
print("The sum of numbers is: " + str(sum_numbers))
