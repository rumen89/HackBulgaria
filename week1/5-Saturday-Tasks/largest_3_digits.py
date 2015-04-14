#largest_3_digits.py

n = input("n = ")
n = int(n)

c = n % 10
print(c)

b = (n // 10) % 10
print(b)

a = ((n // 10) // 10) % 10
print(a)

if a < b < c:
    the_bigger_number = (c * 100 + b * 10 + a)
    print(the_bigger_number)
elif a < c < b:
    the_bigger_number = (b * 100 + c * 10 + a)
    print(the_bigger_number)
elif b < a < c:
    the_bigger_number = (c * 100 + a * 10 + b)
    print(the_bigger_number)
elif b < c < a:
    the_bigger_number = (a * 100 + c * 10 + b)
    print(the_bigger_number)
elif c < a < b:
    the_bigger_number = (b * 100 + a * 10 + c)
    print(the_bigger_number)
else:
    the_bigger_number = (a * 100 + b * 10 + c)
    print(the_bigger_number)


if a < b < c:
    the_smaller_number = (a * 100 + b * 10 + c)
    print(the_smaller_number)
elif a < c < b:
    the_smaller_number = (a * 100 + c * 10 + b)
    print(the_smaller_number)
elif b < a < c:
    the_smaller_number = (b * 100 + a * 10 + c)
    print(the_smaller_number)
elif b < c < a:
    the_smaller_number = (b * 100 + c * 10 + a)
    print(the_smaller_number)
elif c < a < b:
    the_smaller_number = (c * 100 + a * 10 + b)
    print(the_smaller_number)
else:
    the_smaller_number = (c * 100 + b * 10 + a)
    print(the_smaller_number)

