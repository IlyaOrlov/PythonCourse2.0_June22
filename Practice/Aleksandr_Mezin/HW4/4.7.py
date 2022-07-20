def dek(fun):
    def inner(*args, **kwargs):
        print("================")
        res = fun(*args, **kwargs)
        print(res)
        print("================")
        return res
    return inner


@dek
def fun(a, b):
    return a + b


fun(100, 200)
