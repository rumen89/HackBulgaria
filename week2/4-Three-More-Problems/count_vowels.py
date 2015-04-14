#count_vowels.py

string = input("Enter text: ")

vowels_count = 0
vowels = ["a", "e", "i", "o", "u", "y", "A", "E", "I", "O", "U", "Y"]
for ch in string:
    if ch in vowels:
        vowels_count += 1

print("In the string " + string + " there is " + str(vowels_count) + " vowels")
