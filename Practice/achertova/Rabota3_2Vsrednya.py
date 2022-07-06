s = input("Введите пройденный путь в км: ")
t = input("Введите общее время, затраченное на движение в часах: ")
if s.isdecimal() and t.isdecimal():
    vsrednya = float(s) / float(t)
    print(f"Средняя скорость составила {vsrednya} км/ч")
else:
    print("Ошибка ввода. Введите числовые значения без иных символов")



