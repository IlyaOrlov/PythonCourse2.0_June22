def decorator(fun):
    def fun(*args, **kwargs):
        print("=======")
        fun(*args, **kwargs)
        print("=======")


@decorator
def smart(a, b):
    print(a + b)


a = 100
b = 200
print(smart(a, b))








