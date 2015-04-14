#min_of_n.py

n = input("Enter count number: ")
n = int(n)

counter = 0
numbers = []

while counter < n:
    number = input("Enter number: ")
    number = int(number)
    
    numbers += [number]

    counter += 1

min_number = numbers[0]    

for number in numbers:
    if min_number > number:
        min_number = number
    


print("Min number is: " + str(min_number))
