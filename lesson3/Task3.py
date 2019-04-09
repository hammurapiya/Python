'''
3: Давайте опишем пару сущностей player и enemy через словарь, который будет иметь ключи и значения:
name — строка, полученная от пользователя,
health = 100,
damage = 50.

Поэкспериментируйте с значениями урона и жизней по желанию.
Теперь надо создать функцию attack(person1, person2).
Примечание: имена аргументов можете указать свои.
Функция в качестве аргумента будет принимать атакующего и атакуемого.
В теле функция должна получить параметр damage атакующего и отнять это количество от health атакуемого. Функция должна сама работать со словарями и изменять их значения.

'''
player = {
    'name' : input('Введите имя игрока: '),
    'health' : 100,
    'damage' : 20
}

enemy = {
    'name' : input('Введите имя соперника: '),
    'health' : 100,
    'damage' : 50
}

def attack(person1, person2):
    while player['health'] >= 0 or enemy['health']>=0:
        player['health'] = player['health'] - enemy['damage']
        enemy['health'] = enemy['health'] - player ['damage']

    if player['health'] > enemy['health'] :
        print(f'''{player['name']} is winner!''')
    elif player['health'] < enemy['health']:
        print(f'''{enemy['name']} is winner!''')
    else :
        print('Dead heat!')


attack(player,enemy)
