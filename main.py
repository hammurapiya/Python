'''
2. Создайте модуль. В нем создайте функцию, которая принимает список и возвращает из него случайный элемент.
Если список пустой, функция должна вернуть None. Проверьте работу функций в этом же модуле.

'''

import Module1 as m1
from Module2 import get_random, list2, list1

m1.create_folder()
m1.delete_folder()

my_list=[33,66,44]
print(get_random(list1))
print(get_random(list2))
print(get_random(my_list))

