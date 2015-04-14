# triangles.py

# Във файл triangles.py, напишете следните функции, за работа с 
# триъгълници:

# is_triangle(a, b, c) - връща True или False в зависимост от това 
# дали страните a, b и c са страни на триъгълник. Те трябва да спазват 
# неравенството на триъгълника
# area(a, b, c) - връща float, който представлява лицето на триъгълник 
# ъс страни a, b и c. Използвайте Хероновата формула, за да намерите 
# лицето на триъгълника
# is_pythagorean(a, b, c) - проверява дали правоъгълния триъгълник, 
# с катети a и b и хипотенуза c е питагоров. За да е питагоров един 
# триъгълник, той трябва да спазва уравнението a^2 + b^2 = c^2
# max_area(triangles) - взима списък от триъгълници triangles и връща 
# този триъгълник, който е с най-голямо лице от всички. 
# Всеки триъгълник в triangles е представен като списък от 3 елемента. 
# Например, triangles, в който имаме 2 триъгълника ще изглежда така: 
# [ [3, 4, 5], [7, 8, 9] ].
# В последната точка се използва понятието списък то списъци.

# Нека да имаме:

# triangles = [ [3, 4, 5], [7, 8, 9] ]
# То тогава, този израз е равен на списък (първият елемент на triangles):

# first_triangle = triangles[0]
# print(first_triangle) # [3, 4, 5]
# А този израз е равен на първата страна на първия триъгълник:

# first_a_side = triangles[0][0]
# print(first_a_side) # 3

from math import sqrt

def is_trangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True

    return False

def area(a, b, c):
    p = (a + b + c)/2

    S = sqrt(p * (p - a) * (p - b) * (p - c))

    return S

def is_pythagorean(a, b, c):
    triangle_list = [a, b, c]

    triangle_list = sorted(triangle_list)

    if triangle_list[0] ** 2 + triangle_list[1] ** 2 == triangle_list[2] ** 2:
        return True

    return False

def max_area(triangles):
    max_triangle = triangles[0]

    a = max_triangle[0]
    b = max_triangle[1]
    c = max_triangle[2]

    max_area = area(a, b, c)

    for triangle in triangles:
        a = triangle[0]
        b = triangle[1]
        c = triangle[2]

        current_area = area(a, b, c)

        if current_area > max_area:
            max_triangle = triangle
            max_area = current_area

    return max_triangle

# print(max_area([[3, 4, 5], [5, 6, 7], [5, 8, 11]]))