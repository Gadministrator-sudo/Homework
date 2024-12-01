# Цель: написать программу, которая составляет словарь, используя grades и students, где ключом будет имя ученика,
#  а значением - его средний балл

# Начальные данные
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

###

students = sorted(students)
print(students)

def Slovar(students: set, grades: list) -> dict:
    sred_bal = {}
    for i in range(len(grades)):
        sred_bal[students[i]] = sum(grades[i]) / len(grades[i])
    return sred_bal
f = Slovar(students, grades)
print(f)