#only_evens.py

n = input("Enter n:")
n = int(n)

counter = 1
numbers = []

while counter <= n:
    number = input("Enter number: ")
    number = int(number)
    if number%2 == 0:
        
        numbers = numbers + [number]

    counter += 1

print("Count of evens:" + str(len(numbers)))
print ("Evens are:")
print(numbers)
