class A:
    def hello(self):
        print('Hello, A')


class B:
    pass
    # def hello(self):
    #     print('Hello, B')


class C(B, A):
    pass


c = C()
c.hello()
