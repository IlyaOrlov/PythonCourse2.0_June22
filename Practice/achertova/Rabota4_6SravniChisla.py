def fun1(x, y):
    if int(x) > int(y):
        print(f"Большее число {x}")
    else:
        print(f"Большее число {y}")


def fun2(x, y):
    if int(x) > int(y):
        z = x
    else:
        z = y
    return z


while not (a := input("Введите первое число: ")).isdecimal():
    print("Введите числовое целое значение!")
while not (b := input("Введите второе число: ")).isdecimal():
    print("Введите числовое целое значение!")
fun1(a, b)
c = int(fun2(a, b)) * 100
print(f"{fun2(a,b)} * 100 = {c}")
