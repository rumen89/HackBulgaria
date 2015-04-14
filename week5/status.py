# status.py

# Радо е изпаднал в затруднение с курса по Ruby on Rails.

# Системата му е дала списък с всички кандидатствали курсисти и техния статус - 
# дали са си предали задачите или не. 
# Обаче Радо се е объркал и не може да разбере колко са финализираните кандидатури и 
# колко не са.

# Във файл status.py, напишете функция status_count(students), която:

# Взима списък от речници students. Всеки речни в списъка има два ключа - 
# "name" и "status", като статусът може да е "finalized" или "not_finalized".
# Връща речник, които има два ключа - "finalized" и "not_finalized". 
# Срещу всеки речник стои списък от имената на студентите, 
# които имат дадения статус в students

def status_count(students):
    result = {
        "finalized": [],
        "not_finalized": []
    }

    for student_info in students:
        if "finalized" == student_info["status"]:
            result["finalized"] += [student_info["name"]]
        else:
            result["not_finalized"] += [student_info["name"]]

    return result

# print(status_count([{
#               "name": "RadoRado",
#               "status": "not_finalized"
#             }, {
#               "name": "Ivo",
#               "status": "finalized"
#             }, {
#               "name": "Genadi",
#               "status": "finalized"
#             }]))