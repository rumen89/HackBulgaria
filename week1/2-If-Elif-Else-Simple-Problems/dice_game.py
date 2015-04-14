from random import randint

n = input("Enter sides")
n = int(n)

player_1 = input ("Enter player 1 name: ")

player_2 = input ("Enter player 2 name: ")

result_1 = randint (1, n)
result_2 = randint (1, n)


print(result_1)
print(result_2)

if result_1 > result_2:
    print ("Player 1 is a winner")
elif result_2 > result_1:
    print ("Player 2 is a winner")
elif result_1 == result_2:
    print ("No winners")
