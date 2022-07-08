from decorator_example import time_checker, hello_bye


@time_checker
def fun(a, b):
    r = a + b
    return r


def fun2(a, b):
    r = a * b
    return r


input = hello_bye(input)
input("Введите что-нибудь: ")
