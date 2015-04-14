# winter.py

# Вие сте нов синоптик във Вестерос и сте нагърбени със задача, да кажете дали зимата иде.

# Това, което получавате е списък от низове seasons, 
# където всеки елемент ще бъде един от следните низове:

# "winter"
# "summer"
# "spring"
# Във Вестерос има следното правило - зимата иде само, ако са минали най-малко 5 сезона 
# (лято или пролет), след последната зима.

# Сезоните са подредени по хронологичен ред в seasons.

# Например, ако имаме 
# seasons = ["winter", "summer", "summer", "summer", "spring", "srping"], 
# то зимата иде, защото от последната зима са минали 5 други, различни сезона.

# Във файл winter.py, напишете функция winter_is_coming(seasons), 
# която отговаря с True или False на базата на сезоните, които идват.

def winter_is_coming(seasons):
    counter = 0

    for season in seasons:
        if season == "winter":
            counter = 0
        else:
            counter += 1

    return counter >= 5

seasons = ["summer", "spring", "winter", "summer", "summer", "spring", "spring"]
if winter_is_coming(seasons):
    print("Winter is here")
else:
    print("Winter isn't coming")