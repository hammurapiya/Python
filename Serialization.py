'''

1. Создать модуль music_serialize.py. В этом модуле определить словарь для вашей любимой музыкальной группы, например:
my_favourite_group = {
‘name’: ‘Г.М.О.’,
‘tracks’: [‘Последний месяц осени’, ‘Шапито’],
‘Albums’: [{‘name’: ‘Делать панк-рок’,‘year’: 2016},
{‘name’: ‘Шапито’,‘year’: 2014}]}

С помощью модулей json и pickle сериализовать данный словарь в json и в байты, вывести результаты в терминал.
Записать результаты в файлы group.json, group.pickle соответственно. В файле group.json указать кодировку utf-8.
'''

import pickle
import json

my_favourite_group = {
'name': 'Queen',
'tracks': ['Headlong', 'Hammer to fall', 'Scandal' , 'These Are The Days Of Our Lives',
           'Is This The World We Created?', 'Who Wants To Live Forever', 'Don''t Stop Me Now' ],
'Albums': [{'name': 'Innuendo','year': 1991},
            {'name': 'The Miracle','year': 1989},
            {'name': 'Made in Heaven','year': 1995},
            {'name': 'The Works', 'year': 1984}]}

byte_group = pickle.dumps(my_favourite_group)

json_group = json.dumps(my_favourite_group)

print(byte_group)
print(json_group)

with open('group.pickle', 'wb') as f:
    pickle.dump(my_favourite_group, f)

with open('group.json', 'w',  encoding='utf-8') as f:
    json.dump(my_favourite_group, f)