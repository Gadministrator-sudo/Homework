first = int(input('Введите 1 число: '))
second = int(input('Введите 2 число: '))
third = int(input('Введите 3 число: '))

if first == second and second == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
elif first != second !=third:   # Допускается ли такая форма записи, если все прекрасно работает ?
    print(0)
