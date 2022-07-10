a = input("Введите пятизначное число:")

while len(str(a)) != 5 or not a.isdecimal():
    print("Неверное число: ")
    a = input("Введите пятизначное число:")
i = 1
for n in a:
    print(f"{i} цифра равна {n}")
    i += 1
