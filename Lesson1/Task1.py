# Даны два произвольных списка. Удалите из первого списка элементы, присутствующие во втором.
#   Примечание. Списки создайте вручную, например:
# my_list_1 = [2, 5, 8, 2, 12, 12, 4]
# my_list_2 = [2, 7, 12, 3]


my_list_1 = [2, 5, 8, 2, 12, 3, 12, 4]
my_list_2 = [2, 7, 12, 3]

for elem in my_list_2:
    if elem in my_list_1:
        count = my_list_1.count(elem)
        while count>0:
            my_list_1.remove(elem)
            count = count-1

print(my_list_1)
print(my_list_2)