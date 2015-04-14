#words_count.py

input_word = input("Enter word: ")
n = input("Enter number: ")
n = int(n)

count = 1
words = []
words_count = 0

while count <= n:
    word = input("Enter word: ")

    words += [word]

    count = count + 1

for word in words:
    if input_word in word:
        words_count += 1

    print(word)

print(input_word + " is found " + str(words_count) + " times")
