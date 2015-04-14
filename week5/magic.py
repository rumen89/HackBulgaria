# magic.py

def row_sum(matrix, index):
    result = sum(matrix[index])

    return result

def col_sum(matrix, index):
    result = 0

    for row in matrix:
        result += row[index]

    return result

def second_diag(matrix):
    result = 0

    index = len(matrix[0]) - 1

    for row in matrix:
        result += row[index]
        index -= 1

    return result

def main_diag(matrix):
    result = 0

    index = 0

    for row in matrix:
        result += row[index]
        index += 1

    return result

def magic_square(matrix):
    right_sum = main_diag(matrix)

    if second_diag(matrix) != right_sum:
        return False

    for index in range(0, len(matrix)):
        if row_sum(matrix, index) != right_sum:
            return False

    for index in range(0, len(matrix)):
        if col_sum(matrix, index) != right_sum:
            return False

    return True

square1 = [ [23, 28, 21],
            [22, 24, 26],
            [27, 20, 25] ]

# print(magic_square(square1))