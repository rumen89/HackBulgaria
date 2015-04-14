#functions.py

# def main():
#     print(setify([0, 1, 1, 5, 5, 6]) == [0, 1, 5, 6])
#     print(union([0, 0, 0, 0, 0], [1, 2]) == [0, 1, 2])
#     print(intersection([0, 0, 1, 2, 5], [5, 5, 6]) == [5])
#     print(diff([0, 1, 2, 3, 4, 5], [0, 0, 1, 1, 2, 2, 3, 3]) == [4, 5])
#     print(cartesian_product([0, 1], [1]) == [(0, 1), (1, 1)])


# if __name__ == '__main__':
#     main()

def setify(a):
    result = []

    for element in a:
        if element not in result:
            result.append(element)

    return result




def diff(a, b):
    result = []

    for item in setify(a):
        if item not in setify(b):
            result.append(item)

    return result




def union(a, b):
    result = []

    result = setify(a) + setify(b)
    result = setify(result)
    return result




def intersection(a, b):
    result = []

    for element in a:
        if element in b:
            result.append(element)

    result = setify(result)

    return result



def cartesian_product(a, b):
    result = []

    for i in setify(a):
        for j in setify(b):
            result.append((i, j))

    return result



# def main():
#     print(setify([0, 1, 1, 5, 5, 6]) == [0, 1, 5, 6])
#     print(union([0, 0, 0, 0, 0], [1, 2]) == [0, 1, 2])
#     print(intersection([0, 0, 1, 2, 5], [5, 5, 6]) == [5])
#     print(diff([0, 1, 2, 3, 4, 5], [0, 0, 1, 1, 2, 2, 3, 3]) == [4, 5])
#     print(cartesian_product([0, 1], [1]) == [(0, 1), (1, 1)])


# if __name__ == '__main__':
#     main()