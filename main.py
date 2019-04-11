'''
3. Создайте модуль main.py. Из модулей, реализованных в заданиях 1 и 2, сделайте импорт в main.py всех функций.
Вызовите каждую функцию в main.py и проверьте, что все работает как надо.
Примечание: Попробуйте импортировать как весь модуль целиком (например из задачи 1), так и отдельные функции из модуля.
'''

import Module1 as m1
from Module2 import get_random, list2, list1

m1.create_folder()
m1.delete_folder()

my_list=[33,66,44]
print(get_random(list1))
print(get_random(list2))
print(get_random(my_list))

