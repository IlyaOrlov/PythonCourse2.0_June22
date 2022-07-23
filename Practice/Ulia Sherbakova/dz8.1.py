class MyIter:

    def __init__(self, str):
        self.str = str

    def __iter__(self):
        return self

    def __next__(self):
        j = str.split('\t')
        print(j[n])


str = "Поэтому имя можно найти, \t используя разные методы. \t Если вы хотите получить родительский класс, вам нужно передать его ... \t Также вы должны включить self как первый аргумент методов класса. \t Это соглашение python, которое позволяет вам..."
mi = MyIter(str)
it = iter(mi)
n = 0
print(next(it))
n = 1
print(next(it))
n = 2
print(next(it))
