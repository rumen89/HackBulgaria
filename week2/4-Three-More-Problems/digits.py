#digits.py

n = input("Enter some number: ")
n = int(n)

digits = []

while n != 0:
    digit = n % 10

    digits = [digit] + digits

    n = n // 10

print(digits)

counter = 0
number = 0

while counter < len(digits):
    number = number * 10 + digits[counter]
    counter += 1
    
print(number)
