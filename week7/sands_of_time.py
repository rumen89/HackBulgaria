#sands_of_time.py

def sands_of_time(odd_number):
    counter = odd_number

    sands = []

    while counter >= 1:
        sands += ["*" * counter]

        counter -= 2

    result = ""
    counter = 1

    for i in range(0, len(sands)):
        result += "." * counter + sands[i] + "." * counter

        result += "\n"
        counter += 1

    index = len(sands) - 2

    while index >= 0:
        result += "." * (index + 1) + sands[index] + "." * (index + 1) + "\n"

        index -= 1

    return result

n = input("Enter odd number: ")
n = int(n)

# print(sands_of_time(n))