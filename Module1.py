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
