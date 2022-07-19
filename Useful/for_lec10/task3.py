import os


for item in os.listdir('.'):
    if os.path.isfile(item):
        print(f'{item} is file')
    elif os.path.isdir(item):
        print(f'{item} is dir')
