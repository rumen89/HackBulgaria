# coins.py

# Във файл coins.py, напишете функция calculate_coins(sum), където:

# sum е число с плаваща запетая
# Функцията трябва да върне речник, който представлява оптималното представяне на 
# sum чрез минимална бройка монети
# Монетите, с които разполагаме ще са на стойност 1,2,100,5,10,50,20.

def calculate_coins(sum):
    coins = [1,2,100,5,10,50,20]

    coins = sorted(coins, reverse = True)

    sum = round(sum * 100)

    result = {}

    for coin in coins:
        times_to_pay = sum // coin

        result[coin] = times_to_pay

        sum -= times_to_pay * coin

    return result

# n = input("Enter sum: ")
# n = float(n)

# print(calculate_coins(n))