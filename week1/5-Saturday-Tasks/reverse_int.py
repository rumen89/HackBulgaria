#reverse_int.py

n = input("n = ")
n = int(n)

m = 0

while n != 0:
    m = (m * 10) + (n % 10)
    n = n // 10
print(m)
