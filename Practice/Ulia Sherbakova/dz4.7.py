def external(fun):
    def inner(*args, **kwargs):
        print("===========")
        res = fun(*args, **kwargs)
        print(res)
        print("===========")
        return res

    return inner


def fun(a, b):
    return a + b

fun = external(fun)

fun(15, 30)