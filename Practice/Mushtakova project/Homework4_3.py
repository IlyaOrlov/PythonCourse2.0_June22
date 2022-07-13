res = ""
while (a := input("Введите число: ")).lower() != "stop":
    if a.isdecimal():
        res += a
    else:
        print("Предупреждение!")
print(res)


