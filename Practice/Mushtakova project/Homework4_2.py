x = input("Введите пятизначное число: ")
print(x)
if len(x) == 5 and x.isdecimal():
    n = 1
    for i in x:
        print(f"{n} цифра равна {i}")
        n += 1
else:
    print("Некорректное число ")

