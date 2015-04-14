#factorial.py

n = input("Enter some number: ")
n = int(n)

m = 1
factoriel = 1

while m <= n:
    factoriel = factoriel * m
    m = m + 1
print(factoriel)
