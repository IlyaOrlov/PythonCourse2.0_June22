import tempfile
import os


class WrapStrToFile:
    def __init__(self):
        self.filepath = tempfile.mktemp(dir='.')
        print(self.filepath)
        # здесь инициализируется атрибут filepath, он содержит путь до файла-хранилища

    @property
    def content(self):
        try:
            with open(self.filepath, 'r') as f:
                self._content = f.read()
        except FileNotFoundError:
            return "файл не существует"
        else:
            return self._content

    @content.setter
    def content(self, value):
        with open(self.filepath, 'w') as f:
            f.write(value)
            print(f'keep val: {value}')

    @content.deleter
    def content(self):
        os.remove(self.filepath)


wstf = WrapStrToFile()
print(wstf.content)  # Output: File doesn't exist
wstf.content = 'test str'
print(wstf.content)  # Output: test_str
wstf.content = 'text 2'
print(wstf.content)  # Output: text 2
del wstf.content     # после этого файла не существует
