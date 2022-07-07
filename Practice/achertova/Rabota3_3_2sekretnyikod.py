sekretnyikod = input("Введите полученный секретный код, содержащий только цифры: ")
a = 10
if sekretnyikod.isdecimal():
    parol = int(sekretnyikod) ^ a
    print(f"Ваш пароль: {parol}")
else:
    print("Ошибка ввода. Введите числовые значения без иных символов")
