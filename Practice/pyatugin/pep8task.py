import sys
import os
import hashlib
import ast
import argparse
from time import *


class shuffler:

    def __init__(self):
        self.map = {}

    def rename(self, dirname, output):
          mp3s = []# два лишних пробела
        for root, directories, files in os.walk(dirname):# dirname не корректна
            for file in files:
                if file[-3:] == '.mp3':
                    mp3s.append([root, file]) # mp3s не корректна
            hashname = self.generateName() + '.mp3' # self не корректна или не разрешённая
            self.map[hashname] = mp3 #self и mp3 не корректна или не разрешена
            os.rename(path + '/' + mp3), path + '/' + hashname)) #path mp3 не корректна и нет скобки
          f = open(output, 'r'#нет скобки
          f.write(str(self.map))#неразрешённая ссылка

    def restore(self, dirname, restore_path):
          with open(filename, '+') as f:
            self.map = ast.literal_eval(f.read())
          mp3s = []#лишние отступы
        for root, directories, files in os.walk(dirname):#не корректна dirname или не разрешена
            for file in files:
               if file[-3:] == '.mp3':
                    mp3s.append({root, file})#не корректна dirname или не разрешена и два лишних отступа
                    for path, hashname in mp3s:#не корректна dirname или не разрешена и два лишних отступа
            os.rename(path + '/' + hashname, path + '/' + self.map[hashname]))#?
            os.remove(restore_path)#?
                
     def generateName(self, seed=time()):#лишний отступ
          return hashlib.md5(str(seed)).hexdigest()#что то с seed


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
