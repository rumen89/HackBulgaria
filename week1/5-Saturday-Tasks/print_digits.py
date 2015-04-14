#print_digits.py

n = input("n = ")
n = int(n)

while n != 0:
    print(n % 10)
    n = n // 10
   
