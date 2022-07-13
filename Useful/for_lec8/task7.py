class A:
    def __init__(self):
        self.__attr = 100

    def pay(self, sum):
        self.__attr -= sum


a = A()
print(a.__dict__)
# a.__attr = 300
# print(a.__attr)
