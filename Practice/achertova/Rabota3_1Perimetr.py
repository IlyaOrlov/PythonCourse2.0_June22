a = input("Введите длину прямоугольника в см: ")
b = input("Введите ширину прямоугольника в см: ")
if a.isdecimal() and b.isdecimal():
    prmtr: float = 2 * (float(a) + float(b))
    #PyCharm предлагает такую конструкцию, добавить : float -
    # чтобы результат был действительным числом? Это вообще обиходная конструкция?
    print(f"Периметр прямоугольника : {prmtr} см")
    # print(f"Периметр прямоугольника : {round(2[prmtr,2digits])} см")
    # Хотела поставить функцию округления до 2 разряда - не получилось.
    # Подскажите, как это правильно сделать?
else:
    print("Ошибка ввода. Введите числовые значения без иных символов")
