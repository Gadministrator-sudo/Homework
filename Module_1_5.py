immutable_var = ([1,2], 3, True)
print(type(immutable_var))
print(immutable_var)
#immutable_var[2] = False # попытка изменить неизменяемый объект списка приводит к ошибке так как кортеж это неизменяемый список
                         # но он може содержать в себе изменяемые обьекты в моем случае это первый обьект кортежа [1,2]
print(immutable_var)

mutable_list = ([1,2], 3)
mutable_list[0][0] = 2
print(mutable_list)