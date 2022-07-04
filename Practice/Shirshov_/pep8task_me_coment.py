import sys
import os
import hashlib
import ast
import argparse
from time import *


class shuffler:  # имя класса должно быть CamelCase

    def __init__(self):
        self.map = {}

    def rename(self, dirname, output):
          mp3s = []    # убрать лишний пробел (2 шт.)
        for root, directories, files in os.walk(dirname):
            for file in files:
                if file[-3:] == '.mp3':
                    mp3s.append([root, file])
        for path, mp3 in mp3s:
            hashname = self.generateName() + '.mp3'
            self.map[hashname] = mp3
            os.rename(path + '/' + mp3), path + '/' + hashname))    # добавить "(" долно быть os.rename((path + '/'
          f = open(output, 'r')     # убрать пробелы (2 шт.)
          f.write(str(self.map))    # убрать пробелы (2 шт.)

    def restore(self, dirname, restore_path):
          with open(filename, '+') as f:  # убрать пробелы (2 шт.)
            self.map = ast.literal_eval(f.read())  # убрать пробелы (4 шт.) выровнить по with
          mp3s = []  # должен быть выровнен по self.map (удалить пробелы)
        for root, directories, files in os.walk(dirname):
            for file in files:
               if file[-3:] == '.mp3': # добавить пробел
                    mp3s.append({root, file})
        for path, hashname in mp3s:
            os.rename(path + '/' + hashname, path + '/' + self.map[hashname]))  # убрать одну ")" в конце
        os.remove(restore_path)  # добавить пробелы (4 шт.) не уверен, что должна быть в цикле?
                
     def generateName(self, seed=time()):   # убрать пробел
          return hashlib.md5(str(seed)).hexdigest()   # убрать пробелы (2 шт.)


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
# добавить строку
def main():
    args = parse_arguments()
    Shuffler = shuffler()   # необходимо изменить имя класа на соответствующее, которое задано с верху
    if args.subcommand == 'rename':
          if args.output:
                Shuffler.rename(args.dirname, 'restore.info')   # лишний пробелы (2 шт.)
          else:
                Shuffler.rename(args.dirname, args.output)      # лишний пробелы (2 шт.)
    elif args.subcommand == 'restore':
        Shuffler.restore(args.dirname, args.restore_map)
    else:
        sys.exit()
# убрать строчку
# убрать строчку
main()  # добавить пробелы (4 шт.)
