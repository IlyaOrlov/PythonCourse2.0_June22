class MyClass:
    def __init__(self, x):
        self.x = x

    def __call__(self, a, b):
        self._a = a
        self._b = b
        self._res = a + b
        return self._res

    def show_last_op(self):
        print(f'Last op: {self._a} + {self._b} = {self._res}')

    def __add__(self, other):
        return self.x + other.x


m1 = MyClass(5)
print(m1(4, 5))
m1.show_last_op()

m2 = MyClass(7)
print(m1 + m2)