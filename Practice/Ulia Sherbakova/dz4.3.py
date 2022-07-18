while (s := input("Введите число: ")).lower() != 'stop':
    if s.isdecimal():
       print(f"{s}")
    else:
       print("Я просил число, попробуй снова")