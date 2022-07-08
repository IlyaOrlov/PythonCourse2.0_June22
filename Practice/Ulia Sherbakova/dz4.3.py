while (s := input("Введите символ: ")) != 'stop' and s != 'Stop' and s!= 'STOP':
    if s.isdecimal():
       print(f"{s}")
    else:
       print("Я просил число, попробуй снова")