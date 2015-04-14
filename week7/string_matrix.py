# string_matrix.py

# Във файл с име string_matrix.py, напишете програма,
# в която има следната функция string_matrix(matrix_width, strings).

# Функцията взима като аргументи число и списък от стирнгове, а връща :

# матрица, с размери подадето число и с елементи - char-овете на подадените стрингове.
# на всеки ред от матрицата трябва да се намира само по един стринг. 
# Ако дължината му е по-голяма от големината на матрицата, го отрежете до подходяща.
# Ако е с по-малка дължина - допълнете реда на матрицата с "X".

# Пример:

# >>> result = string_matrix(6,["python","gogo","perl","java","haskell","ruby0nRails"])
# >>> print(result)
# | p | y | t | h | o | n |
# | g | o | g | o | X | X |
# | p | e | r | l | X | X |
# | j | a | v | a | X | X |
# | h | a | s | k | e | l |
# | r | u | b | y | O | n |

def to_matrix(n, list):
    result = []
    while True:
        for string in list:
            characters = []

            i = 0

            while i < n:
                if i >= len(string):
                    characters += ["X"]
                else:
                    characters += [string[i]]

                i += 1

            result += [characters]

        m = n

        if m > len(list):
            while m - len(list) > 0:
                result += [["X"] * n]
                m -= 1

        if len(result) == n:
            break

    return result

def string_matrix(matrix):
    result = ""

    for row in matrix:
        for element in row:
            result += "| " + element + " "

        result += "|" + "\n"

    return result

# print(string_matrix(to_matrix(7,["python","gogo","perl","java","haskell","ruby0nRails"])))