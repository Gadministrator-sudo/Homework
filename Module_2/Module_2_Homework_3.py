my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6,5]
i = 0
#while i < len(my_list):
#    if my_list[i] > 0:
#        print(my_list[i])
#    if my_list[i] == 0:
#        print()
#    if my_list[i] < 0:
#        print()
#    i = i + 1

#while i < len(my_list):
#    if my_list[i] < 0:
#        print()
#    elif my_list[i] != 0:
#        print(my_list[i])
#    i = i + 1

while i < len(my_list):
    if my_list[i] > 0 and my_list[i] != 0:
        print(my_list[i])
    i = i + 1
    if my_list[i] < 0 :
        break
