#bigger_last_digit.py

n = input("Write a number n: ")
m = input("Write a number m: ")
n = int(n)
m = int(m)

if n % 10 > m % 10:
    print(n)
elif n % 10 < m % 10:
    print(m)
elif n % 10 == m % 10:
    if n > m:
        print(n)
    elif n < m:
        print(m)
    else:
        print("equal")
