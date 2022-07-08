def fun1(a, b):
    if a > b:
        print(a)
    elif b > a:
        print(b)

def fun2(c, d):
    if c > d:
        return c
    elif d > c:
        return d

fun1(6,4)
print(fun2(4,6))

