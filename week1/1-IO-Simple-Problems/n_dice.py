#n_dice.py

n = input ("Enter sides for dice: ")
n = int (n)

from random import randint
result = randint (1, n)

print ("The dice rolled:")
print (result)
