# Пункт 2. Работа со словарями

my_dict = {'Tolik' : 1994 , 'Sasha' : 1991}
print(my_dict)

print('Existing value:' , my_dict.get('Tolik'))
print(my_dict.get('Anton', 'Not existing value'))

my_dict.update({'Vova' : 2021,
                'Leva' : 2023})
print(my_dict)

a = my_dict.pop('Tolik')
print('Deleted value:',a)
print('Modified dictionary',my_dict)



# Пункт 3. Работа со множествами

my_set = {1, 2, 3, 2, 1,'Tolik',42.1}
print('Set', my_set)

my_set.add(5)
my_set.add('String')
my_set.discard('Tolik')
print('Modified set', my_set)
