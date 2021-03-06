# tic.py

# Морски шах е известна игра, която се играе в 3x3 матрица (дъска / квадрат, 
# където се слагат X и O.

# Във файла tic.py, напишете следната функция:

# board_to_string(board)
# Функцията взима една матрица с размерности 3x3 и връща низ, който представлява дъската,
# като между всеки ред има символ за нов ред - \n.

# Всеки ред има по 3 елемента, които може да са X, О или празно квадратче #

# Например:

# board = [ ["X", "O", "#"],
#           ["X", "X", "X"],
#           ["#", "#", "#"] ]

# result = board_to_string(board)

# print(result)
# result трябва да има следната стойност:

# "X|O|#\nX|X|X\n#|#|#"
# На екрана трябва да се изведе следния резултат:

# X|0|#
# X|X|X
# #|#|#
# Втора стъпка - разстояние между квадратите

# След като сте готови с горната задача, модифицирайте board_to_string по следния начин, 
# така че крайният резултат да изглежда така:

# X | 0 | #
# X | X | X
# # | # | #
# Всяка клета трябва да има отстояние от 1 празно пространство, за елемента вътре.

# Трета стъпка - крайните стени

# След като сте готови със втора стъпка, модифицирайте board_to_string по следния начин, 
# така че крайният резултат да изглежда така:

# | X | 0 | # |
# | X | X | X |
# | # | # | # |
# Трябва да се добавят и крайните стени

def board_to_string(board):
    result = ""

    for row in board:
        for element in row:
            result += "| " + str(element) + " "

        result += "|" + "\n"

    return result

board = [ ["X", "O", "#"],
          ["X", "X", "X"],
          ["#", "#", "#"] ]

print(board_to_string(board))