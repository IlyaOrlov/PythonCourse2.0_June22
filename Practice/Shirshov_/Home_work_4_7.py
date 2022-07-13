def start_stop(original_fun):
    def inner(*args, **kwargs):
        print("=================")
        res = original_fun(*args, **kwargs)
        print(res)
        print("=================")
        return res

    return inner


@start_stop
def su(mes1, mes2, mes3):
    return (mes1 + mes2)/mes3


su(10, 20, 4)