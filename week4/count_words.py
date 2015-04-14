#count_words.py

# Във файл count_words.py, напишете функция count_words(words), която:

# Взима списък от низове words
# Връща речник, който има следния вид:
# {
#   "word": count_of_that_word
# }
# За всеки елемент от списъка, се пази броят на неговите срещания в words.

def count_words(words):
    result = {}

    for word in words:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1

    return result

# words = ["word", "house", "mouse", "apple", "house", "word", "apple", "mouse", "mouse", "strawberry"]
# print(count_words(words))