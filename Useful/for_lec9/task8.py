class MyIter:
    def __init__(self, n):
        self.i = 0
        self.cnt = 0
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.cnt < self.n:
            res = self.i
            self.i += 2
            self.cnt += 1
            return res
        else:
            raise StopIteration


n = 3
mi = MyIter(n)
for i in mi:
    print(i)
# it = iter(mi)
# print(it)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
