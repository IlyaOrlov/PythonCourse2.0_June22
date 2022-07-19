import tempfile


class WrapStrToFile:
    def __init__(self):
        self.filepath = tempfile.mktemp(dir='.')
        print(self.filepath)
        # здесь инициализируется атрибут filepath, он содержит путь до файла-хранилища

    @property
    def content(self):

        with open(self.filepath, 'r') as f:
            self._content = f.read()
        # попытка чтения из файла, в случае успеха возвращаем содержимое
        # в случае неудачи возвращаем 'File doesn't exist'

    @content.setter
    def content(self, value):
        # попытка записи в файл указанного содержимого
        pass

    @content.deleter
    def content(self):
        pass
        # удаляем файл: os.remove(имя_файла)


wstf = WrapStrToFile()
print(wstf.content)  # Output: File doesn't exist
# wstf.content = 'test str'
# print(wstf.content)  # Output: test_str
# wstf.content = 'text 2'
# print(wstf.content)  # Output: text 2
# del wstf.content     # после этого файла не существует
