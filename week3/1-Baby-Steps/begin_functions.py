#begin_functions.py

def square(n):
    return n ** 2

def fact(n):
    counter = 1
    factorial = 1
    
    while counter <= n:
        factorial *= counter

        counter += 1

    return factorial

def count_element(items):
    counter = 0

    for item in items:
        counter += 1

    return counter

def memb(x,xs):
    index = False
    for item in xs:
        if x == item:
            index = True
            break
    return index

def grades_that_pass(students, grades, limit):
    result = []
    counter = 0

    for grade in grades:
        student = students[index]

        if grade > limit:
            result += [student]

        counter += 1

    return result
