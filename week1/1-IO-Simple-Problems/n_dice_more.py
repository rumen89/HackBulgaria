#n_dice_more.py

n = input ("Enter sides for dice: ")
n = int (n)

from random import randint

result_1 = randint (1, n)
print ("the dice rolled: " + str(result_1))

result_2 = randint (1, n)
print ("the dice rolled: " + str(result_2))

result_3 = randint (1, n)
print ("The dice rolled: " + str(result_3))

print ("Sum is: " + str(result_1 + result_2 + result_3))
