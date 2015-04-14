#twin_prime.py

p = input("Enter number: ")
p = int(p)

q = p - 2
q1 = p + 2
counter = 2
index_p = True

while counter < p:
    if p % counter == 0:
        index_p = False

    counter += 1

if index_p:
    print("Twins primes with " + str(p))
else:
    print(str(p) + " is not a prime.")

index_q = True
counter = 2

while counter < q:
    if q % counter == 0:
        index_q = False

    counter += 1

if index_q:
    print(str(q) + ", " + str(p) + ":")
else:
    print(str(q) + " is not prime.")
    
index_q1 = True
counter = 2

while counter < q1:
    if q1 % counter == 0:
        index_q1 = False

    counter += 1

if index_q1:
    print(str(p) + ", " + str(q1))
else:
    print(str(q1) + " is not prime.")
