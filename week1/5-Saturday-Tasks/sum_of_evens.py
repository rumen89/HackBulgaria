#sum_of_evens.py

n = input("Enter number: ")
n = int(n)

counter = 2
sum_evens = 0

while counter <= n:
    if counter % 2 == 0:
        sum_evens += counter

    counter += 1

print("The sum of all evens numbers in interval is: " + str(sum_evens))
