a = input("Введите пятизначное число: ")
i = 0
if not len(a) == 5 or not a.isdecimal():
    a = input("Будьте внимательны! Введите пятизначное число еще раз: ")
for n in a:
    i += 1
    print(f"{i} цифра равна {n}")
