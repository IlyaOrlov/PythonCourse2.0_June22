import tempfile
import os, sys

class WrapStrToFile:
    def __init__(self):
        self.filepatch = tempfile.mktemp(dir='.')
        print(self.filepatch)
        # здесь инициализируется атрибут filepath, он содержит путь до файла-хранилища

    @property
    def content(self):
        try:
            with open(self.filepatch, 'r') as f:
                self._content = f.read()
        except FileNotFoundError:
            return(f"Файл еще не существует")
        else:
            return(self._content)

        # попытка чтения из файла, в случае успеха возвращаем содержимое
        # в случае неудачи возвращаем 'File doesn't exist'

    @content.setter
    def content(self, value):
        with open(self.filepatch, 'w') as f:
            self._content = f.write(value)
        # попытка записи в файл указанного содержимого

    @content.deleter
    def content(self):
        os.remove(self.filepatch)
        # удаляем файл: os.remove(имя_файла)


wstf = WrapStrToFile()
print(wstf.content)  # Output: File doesn't exist
wstf.content = 'test str'
print(wstf.content)  # Output: test_str
wstf.content = 'text 2'
print(wstf.content)  # Output: text 2
del wstf.content     # после этого файла не существует
