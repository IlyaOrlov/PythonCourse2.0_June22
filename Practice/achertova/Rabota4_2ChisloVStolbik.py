a = input("Введите пятизначное число: ")
while not len(a) == 5 or not a.isdecimal():
    a = input("Будьте внимательны! Введите пятизначное число еще раз: ")
i = 0
for n in a:
    i += 1
    print(f"{i} цифра равна {n}")
