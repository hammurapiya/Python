'''
Давайте усложним предыдущее задание. Измените сущности, добавив новый параметр — armor = 1.2 (величина брони персонажа)
Теперь надо добавить новую функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
Следовательно, у вас должно быть 2 функции:
1. Наносит урон. Это улучшенная версия функции из задачи 3.
2. Вычисляет урон по отношению к броне.
'''

player = {
    'name' : input('Введите имя игрока: '),
    'health' : 100,
    'damage' : 50,
    'armor' : 5
}

enemy = {
    'name' : input('Введите имя соперника: '),
    'health' : 100,
    'damage' : 50,
    'armor' : 1.2
}

def true_damage(damage_par, armor_par):
    return damage_par/armor_par


def attack(person1, person2):


    while player['health'] >= 0 or enemy['health']>=0:
        PlayerDamage = true_damage(player['damage'],enemy['armor'])
        EnemyDamage = true_damage(enemy['damage'],player['armor'])
        player['health'] = player['health'] - EnemyDamage
        enemy['health'] = enemy['health'] - PlayerDamage

    if player['health'] > enemy['health'] :
        print(f'''{player['name']} is winner!''')
    elif player['health'] < enemy['health']:
        print(f'''{enemy['name']} is winner!''')
    else :
        print('Dead heat!')


attack(player,enemy)