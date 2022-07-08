while not (a := input("Введите цифровой пароль: ")).isdecimal():
    pass
    print("Ваш пароль некорректен")
if a.isdecimal():
    b = int(a) << 1
    print(f"Ваш секретный идентификатор: {b}")

while not (b := input("Введите секретный идентификатор:")):
    pass
if b == b:
    print(f"Ваш пароль: {a}")
