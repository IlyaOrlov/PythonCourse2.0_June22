parol = input("Введите пароль, содержащий только цифры: ")
a = 10
if parol.isdecimal():
    sekretnyikod = int(parol) ^ a
    print(f"Секретный код: {sekretnyikod}")
else:
    print("Ошибка ввода. Введите числовые значения без иных символов")
