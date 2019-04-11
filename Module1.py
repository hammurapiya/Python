'''
1. Создайте модуль (модуль — программа на Python, т.е. файл с расширением .py).
В нем напишите функцию, создающую директории от dir_1 до dir_9 в папке, из которой запущен данный код.
Затем создайте вторую функцию, удаляющую эти папки. Проверьте работу функций в этом же модуле.

'''

import sys
import os

def create_folder():
    for i in range (1,10):
        new_path = os.path.join(os.getcwd(), 'dir_{}'.format(i))
        os.mkdir(new_path)

def delete_folder():
    for i in range (1,10):
        new_path = os.path.join(os.getcwd(), 'dir_{}'.format(i))
        os.rmdir(new_path)

#create_folder()
#delete_folder()
