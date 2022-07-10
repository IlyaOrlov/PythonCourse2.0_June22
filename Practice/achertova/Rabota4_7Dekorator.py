def stroka(fun):
    def inner(*args, **kwargs):
        print("===========")
        res = fun(*args, **kwargs)
        return res
    return inner()


stroka(fun)
