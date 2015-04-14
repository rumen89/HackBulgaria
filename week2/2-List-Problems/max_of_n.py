#max_of_n.py

n = input("Enter count number: ")
n = int(n)

counter = 0
numbers = []

while counter < n:
    number = input("Enter number: ")
    number = int(number)
    
    numbers += [number]

    counter += 1

    max_number = numbers[0]

for number in numbers:
    if max_number < number:
        max_number = number

print("Max number is: " + str(max_number))

