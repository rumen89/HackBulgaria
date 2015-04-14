#sum_digits_interval.py

N = input("N = ")
M = input("M = ")
N = int(N)
M = int(M)

if N > M:
    while M <= N:
        start = M
        sum_of_digits = 0

        while start != 0:
            digit = start % 10

            sum_of_digits += digit

            start = start // 10
        print("Sum of digits of " + str(M) + " is: " + str(sum_of_digits))
        M += 1

elif M > N:
    while N <= M:
        sum_of_digits = 0
        start = N

        while start != 0:
            digit = start % 10

            sum_of_digits += digit

            start = start // 10

        print("Sum of digits of " + str(N) + " is: " + str(sum_of_digits))
        N += 1
