#sum_digits.py

n = input("n = ")
n = int(n)

sum = 0

while n != 0:
    sum = sum + (n % 10)
    n = n // 10
    
print(sum)

