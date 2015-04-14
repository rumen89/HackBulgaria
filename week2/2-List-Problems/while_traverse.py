#while_traverse.py

books = ["Learn You a Haskell", "The Healthy Programmer", "Code Complete", "The pragmatic Programmer", "Pro Git", "Introduction to Algorithms", "Concrete Mathematics"]

start = 0

end = len(books)

while start < end:
    book = books[start]
    print(book)
    start += 1
