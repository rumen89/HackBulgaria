#sum_of_odds.py

n = input("Enter a number: ")
n = int(n)

counter = 1
sum = 0

while counter <= n:
    counter = counter + 1
    if counter % 2 != 0:
        print(counter)
        sum = sum + counter
print("The sum is: " + str(sum))
