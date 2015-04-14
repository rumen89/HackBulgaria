#sorted_names.py

n =input("Enter number: ")
n = int(n)

count = 1
names = []

while count <= n:
    name = input("Enter name: ")

    names += [name]

    count += 1

names = sorted(names)

for name in names:
    print(name)
