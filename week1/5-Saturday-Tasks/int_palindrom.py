#int_polindrom.py

n = input("Enter some number: ")
n = int(n)

m = 0
digit = n

while digit != 0:
    m = (m * 10) + (digit % 10)
    digit = digit // 10
print(m)
if n == m:
    print("The number is polindrom")
else:
    print("The number is not polindrom")
