# count.py

# Във файл count.py напишете функция count_vowels_consonants(word), която:

# Взима един низ word
# Връща речник, в който има два ключа - "vowels" и "consonants"
# Срещу всеки ключ, трябва да стои съответния брой на гласни и съгласни букви в думата.
# Бройте както главните, така и малките гласни и съгласни букви:

# Гласните са "aeiouyAEIOUY"
# Съгласните са "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"

def count_vowels_consonants(word):
    result = {
        "vowels": 0,
        "consonants": 0
    }

    vowels = "aeiouyAEIOUY"
    consonants = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"

    for ch in word:
        if ch in vowels:
            result["vowels"] += 1
        else:
            result["consonants"] += 1

    return result

# word = "akldkfkcmdf"
# print(count_vowels_consonants(word))