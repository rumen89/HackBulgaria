#dice_1001.py

from random import randint

Ivan_score = 1001
Maria_score = 1001

while True:

    counter = 1
    dice_sum = 0

    while counter <= 5:
        dice_rolled = randint(1, 6)
        print("Maria dice rolled: " + str(dice_rolled))

        dice_sum = dice_sum + dice_rolled
       
        counter += 1
    
    if Maria_score > 0:
        Maria_score -= dice_sum
    elif Maria_score < 0:
        Maria_score += dice_sum
    
    print("The sum of Maria dices is: " + str(dice_sum))
    print("Maria score is: " + str(Maria_score))

    counter = 1
    dice_sum = 0

    while counter <= 5:
        dice_rolled = randint(1, 6)
        print("Ivan dice rolled: " + str(dice_rolled))

        dice_sum = dice_sum + dice_rolled
        
        counter += 1
    
    if Ivan_score > 0:
        Ivan_score -= dice_sum
    elif Ivan_score < 0:
        Ivan_score += dice_sum

    print("The sum of Ivan dices is: " + str(dice_sum))
    print("Ivan score is: " + str(Ivan_score))

    if Maria_score == 0:
        print("Maria is winner")
        break

    if Ivan_score == 0:
        print("Ivan is winner")
        break
