#program.py

first_name = input("Enter your first name: ")
second_name = input("Enter your second name: ")
third_name = input("Enter your third name: ")
birth_year = input("Enter your date of birth: ")
birth_year = int(birth_year)
current_year = input("Enter current year: ")
current_year = int(current_year)
age = current_year - birth_year

result = {
    "first name": first_name,
    "second name": second_name,
    "third name": third_name,
    "birth year": birth_year,
    "current age": age
}

# print(result)