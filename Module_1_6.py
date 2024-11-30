# Пункт 2. Работа со словарями

mi_dict = {'Tolik' : 1994 , 'Sasha' : 1991}
print(mi_dict)

#  Выведите на экран одно значение по существующему ключу, одно по отсутствующему из словаря my_dict без ошибки.
# // Не совсем понял вторую часть задания
#mi_dict['Anton'] = 1992
print(mi_dict['Tolik'],['Anton'])


mi_dict.update({'Vova' : 2021,
                'Leva' : 2023})
print(mi_dict)

a = mi_dict.pop('Tolik')
print(a)
print(mi_dict)

# Пункт 3. Работа со множествами
