#n = int(input('Введите количество строк: '))
#m = int(input('Введите количество столбцов: '))
#value = input('Введите значение элементов: ')
#print('------' * m)

def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    print(matrix)
    return matrix


result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

#if n <= 0:
#    print("Количество строк не может быть меньше 0: ", n)
#elif m <=0:
#     print("Количество столбцов не может быть меньше 0: ", m)
#else:
#    print("Матрица воплоти")
#    for i in matrix:
#        print(*i)
