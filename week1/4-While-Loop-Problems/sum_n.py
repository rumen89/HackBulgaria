#sum_n.py

n = input("Enter number: ")
n = int(n)

counter = 1

sum = 0

while counter <= n:
    sum = sum + counter
    counter = counter + 1
print(sum)
