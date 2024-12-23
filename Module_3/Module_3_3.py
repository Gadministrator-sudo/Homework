
def print_params(a = 1, b ='строка', c = True ):      #1.1
    print(a, b, c)                                    #1.2

print_params()                                        #1.3
print_params(1,'Елка', False)                #1.3
print_params('2', 3)                            #1.3

print_params(b = 25)                                  #1.4
print_params(c = [1, 2, 3])                           #1.4

values_list = [2, 'столбец', False]                   #2.1
value_dict = { 'a': 2, 'b': 'столб', 'c': 22.5 }      #2.2

print_params(*values_list)                            #2.3
print_params(**value_dict)                            #2.3

values_list_2 = [2, True]                             #3.1

print_params(*values_list_2, 42)                   #3.2


