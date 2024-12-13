n = int(input("Введите число от 3 до 20: "))
list_ = []
for i in range(1, 21):
    for j in range(2, 21):
        if n % (j + i) == 0 and i < j:
            list_.append(i)
            list_.append(j)
            j = j + 1
        else:
            continue
    i = i + 1
    continue
print(list_)