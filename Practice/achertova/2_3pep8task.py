import sys
import os
import hashlib
import ast
import argparse
from time import *
# не знаю почему, на лекции такой как последний импорт Вам не понравился

class shuffler:
# имя класса не CamelCase, видимо, ожидается написание с большой буквы?
    def __init__(self):
        self.map = {}

    def rename(self, dirname, output):
          mp3s = []
#не выровнена, непонятно по чему дб выровнена
        for root, directories, files in os.walk(dirname):
            for file in files:
                if file[-3:] == '.mp3':
                    mp3s.append([root, file])
# не выровнена, непонятно по чему дб выровнена
        for path, mp3 in mp3s:
            hashname = self.generateName() + '.mp3'
            self.map[hashname] = mp3
            os.rename(path + '/' + mp3), path + '/' + hashname))
#неправильно расположены скобки, дб только первая и последняя
          f = open(output, 'r')
# не выровнена, непонятно по чему дб выровнена
          f.write(str(self.map))
# не выровнена, непонятно по чему дб выровнена

    def restore(self, dirname, restore_path):
          with open(filename, '+') as f:
            self.map = ast.literal_eval(f.read())
          mp3s = []
# не выровнена, непонятно по чему дб выровнена
        for root, directories, files in os.walk(dirname):
            for file in files:
               if file[-3:] == '.mp3':
                    mp3s.append({root, file})
# не выровнена, непонятно по чему дб выровнена
        for path, hashname in mp3s:
            os.rename(path + '/' + hashname, path + '/' + self.map[hashname]))
            # неправильно расположены скобки, дб только первая и последняя
        os.remove(restore)
     
     def generateName(self, seed=time()):
    #имя функции дб в нижнем регистре, без заглавных букв
          return hashlib.md5(str(seed)).hexdigest()


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

def main():
    args = parse_arguments()
    Shuffler = shuffler()
    # имя функции дб в нижнем регистре, без заглавных букв
    if args.subcommand == 'rename':
          if args.output:
                Shuffler.rename(args.dirname, 'restore.info')
          else:
                Shuffler.rename(args.dirname, args.output)
    elif args.subcommand == 'restore':
        Shuffler.restore(args.dirname, args.restore_map)
    else:
        sys.exit()


main()
