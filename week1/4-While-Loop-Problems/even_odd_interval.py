#even_odd_interval.py

a = input("Enter the first number: ")
a = int(a)

b = input("Enter the second number: ")
b = int(b)

if a > b:
    while b <= a:
        if b % 2 == 0:
            print(str(b) + " Even")
        else:
            print(str(b) + " Odd")
        b = b + 1

elif b > a:
    while a <= b:
        if a % 2 == 0:
            print(str(a) + " Even")
        else:
            print(str(a) + " Odd")
        a = a + 1
else:
    print("This isn't the target")
