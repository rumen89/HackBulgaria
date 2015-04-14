#user_to_user.py

a = input("Enter first number: ")
a = int(a)

b = input("Enter second number: ")
b = int(b)

if a > b:
    while b <= a:
        print(b)
        b += 1
elif b > a:
    while a <= b:
        print(a)
        a += 1
else:
    print("Are you stupid? The two numbers are qual!")
