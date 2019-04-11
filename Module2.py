'''
2. Создайте модуль. В нем создайте функцию, которая принимает список и возвращает из него случайный элемент.
Если список пустой, функция должна вернуть None. Проверьте работу функций в этом же модуле.

'''
from random import choice

list1 = [0,5,8,78,9]
list2 = []
def get_random(input_list):
    if len(input_list) != 0:
        return choice(input_list)
    else:
        return None

#print(get_random(list1))
#print(get_random(list2))



