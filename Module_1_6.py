# Пункт 2. Работа со словарями

my_dict = {'Tolik' : 1994 , 'Sasha' : 1991}
print(my_dict)

#  Выведите на экран одно значение по существующему ключу, одно по отсутствующему из словаря my_dict без ошибки.
# // Не совсем понял вторую часть задания
#my_dict['Anton'] = 1992
print(my_dict['Tolik'],['Anton'])


my_dict.update({'Vova' : 2021,
                'Leva' : 2023})
print(my_dict)

a = my_dict.pop('Tolik')
print(a)
print(my_dict)

# Пункт 3. Работа со множествами

my