s1 = ""
while True:
    s = input("Введите число: ")
    if s.lower() == 'stop':
        print(f"результат {s1}")
        break
    elif not s.isdecimal():
        print("Нужно ввести число")
    else:
        s1 += s
