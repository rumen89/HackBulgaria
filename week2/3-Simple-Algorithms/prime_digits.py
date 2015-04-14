#prime_digits.py

n = input("Enter number: ")
n = int(n)

digits = []

while n != 0:
    number = n % 10

    digits = [number] + digits

    n = n // 10

has_prime_digits = False

for number in digits:
    if number in [2, 3, 5, 7]:
        has_prime_digit = True
        break

if has_prime_digit:
    print("At least one prime digit found")
else:
    print("No prime digit found")

    
    
