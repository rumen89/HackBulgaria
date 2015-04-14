#compare.py

a = input ("Write the first number: ")
b = input ("Write the second number: ")

a = int (a)
b = int (b)

print (a)
print (b)

if a > b:
    print ("a " + "(" + str(a) + ")" + " is bigger than " + "b " + "(" + str(b) + ")")
elif a < b:
    print ("b " + "(" + str (b) + ")" + " is bigger than " + "a " + "(" + str (a) + ")")
elif a == b:
    print ("a " + "(" + str (a) + ")" + " is equal to " + "b " + "(" + str (b) +  ")")
