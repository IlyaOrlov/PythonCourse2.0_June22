#  0  1     1  2  3  5
#|     |
#    |        |
class Fibonacci:

    def __init__(self, N):
        self.n, self.a, self.b, self.max = 0, 0, 1, N

    def __iter__(self):
        # сами себе итератор: в классе есть метод next()
        return self

    def __next__(self):
        if self.n < self.max:
            a = self.a
            self.n = self.n + 1
            self.a, self.b = self.b, self.a + self.b
            return a
        else:
            raise StopIteration


for i in Fibonacci(100):
    print(i, end=' ')

# f = Fibonacci(3)
# it_f = iter(f)
# print(next(it_f))
# print(f.a, f.b)
# print(next(it_f))
# print(f.a, f.b)
# print(next(it_f))
# print(f.a, f.b)
# print(next(it_f))
# print(f.a, f.b)
