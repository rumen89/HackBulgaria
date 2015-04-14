#calculator.py

a = input ("Enter a: ")
b = input ("Enter b: ")
operator = input ("Enter operator (+, -, *, /): ")
a = int (a)
b = int(b)

if operator == "+":
    print (a + b)
elif operator == "-":
    print (a - b)
elif operator == "*":
    print (a * b)
elif operator == "/":
    print (a / b)
else:
    print("Something is wrong")
