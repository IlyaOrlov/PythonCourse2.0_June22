def dek(fun):
    def inner(*args, **kwargs):
        print("================")
        res = fun(*args, **kwargs)
        print(res)
        print("================")
        return res
    return inner


def fun(a, b):
    return a + b


fun = dek(fun)

fun(100, 200)
