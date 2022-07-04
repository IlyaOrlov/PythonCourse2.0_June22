import sys
import os
import hashlib
import ast
import argparse
from time import *


class Shuffler:  # изменил имя класса должно быть CamelCase

    def __init__(self):
        self.map = {}

    def rename(self, dirname, output):
        mp3s = []    # убрал лишний пробел (2 шт.)
        for root, directories, files in os.walk(dirname):
            for file in files:
                if file[-3:] == '.mp3':
                    mp3s.append([root, file])
        for path, mp3 in mp3s:
            hashname = self.generateName() + '.mp3'
            self.map[hashname] = mp3
            os.rename((path + '/' + mp3), (path + '/' + hashname))
        f = open(output, 'r')     # сдвиг убрал пробелы (2 шт.)
        f.write(str(self.map))    # сдвиг убрал пробелы (2 шт.)

    def restore(self, dirname, restore_path, filename):
        with open(filename, '+') as f:  # убрать пробелы (2 шт.)
            self.map = ast.literal_eval(f.read())
        mp3s = []  # должен быть выровнял по with
        for root, directories, files in os.walk(dirname):
            for file in files:
                if file[-3:] == '.mp3':   # добавил пробел
                    mp3s.append({root, file})
        for path, hashname in mp3s:
            os.rename(path + '/' + hashname, path + '/' + self.map[hashname])  # убрал одну ")" в конце
        os.remove(restore_path)  # добавить пробелы (4 шт.)
                
    def generateName(self, seed=time()):   # убрал пробел
        return hashlib.md5(str(seed)).hexdigest()   # убрал пробелы (2 шт.)


def parse_arguments():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='subcommand', help='subcommand help')
    rename_parser = subparsers.add_parser('rename', help='rename help')
    rename_parser.add_argument('dirname')
    rename_parser.add_argument('-o', '--output', help='path to a file where restore map is stored')
    restore_parser = subparsers.add_parser('restore', help="command_a help")
    restore_parser.add_argument('dirname')
    restore_parser.add_argument('restore_map')
    args = parser.parse_args()
    return args

# добавил строку
def main(shuffler):
    args = parse_arguments()
    Shuffler = shuffler()   # необходимо изменить имя класcа на соответствующее, которое задано с верху
    if args.subcommand == 'rename':
          if args.output:
              Shuffler.rename(args.dirname, 'restore.info')   # лишний пробелы (2 шт.)
          else:
              Shuffler.rename(args.dirname, args.output)      # лишний пробелы (2 шт.)
    elif args.subcommand == 'restore':
        Shuffler.restore(args.dirname, args.restore_map)
    else:
        sys.exit()
    main()  # добавил пробелы (4 шт.)
