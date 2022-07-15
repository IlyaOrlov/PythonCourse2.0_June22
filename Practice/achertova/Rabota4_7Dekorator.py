def stroka(fun):
    def inner(a, b):
        print("===========")
        res = fun(a, b)
        print(f"{fun(a, b)}")
        print("===========")
        return res

    return inner


def fun(a, b):
    return a + b


fun = stroka(fun)

fun(1, 2)
