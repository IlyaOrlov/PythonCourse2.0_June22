import os
import tempfile


class WrapStrToFile:
    def __init__(self):
        self.filepath = tempfile.mktemp(dir=".")
        # здесь инициализируется атрибут filepath, он содержит путь до файла-хранилища

    @property
    def content(self):
        try:
            with open(self.filepath, "r") as f:
                self._content = f.read()
        except FileNotFoundError:
            return print(f"File doesn't exist")
        else:
            return self._content

        # попытка чтения из файла, в случае успеха возвращаем содержимое
        # в случае неудачи возвращаем 'File doesn't exist'

    @content.setter
    def content(self, value):
        with open(self.filepath, "w") as f:
            self._content = f.write(value)
            return self.content
        # попытка записи в файл указанного содержимого

    @content.deleter
    def content(self):
        os.remove(self.filepath)
        # удаляем файл: os.remove(имя_файла)


wstf = WrapStrToFile()
print(wstf.content)  # Output: File doesn't exist
wstf.content = 'test str'
print(wstf.content)  # Output: test_str
wstf.content = 'text 2'
print(wstf.content)  # Output: text 2
del wstf.content     # после этого файла не существует