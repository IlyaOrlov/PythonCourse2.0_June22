# Программа для расчёта периметра прямоугольника по введённым длине и ширине


def perimeter(a, b):
    return (int(a) + int(b)) * 2


def check_val(val):
    global flag1
    while val.isdecimal() == True:
        flag1 = True
        return val
        break
    else:
        print(val, "Будьте внимательнее, вводите только цифры!")
        flag1 = False


print("Программа для расчёта периметра прямоугольника")


Flag_start = True
while Flag_start:
    a = input("Введите длину прямоугольника: ")
    a = check_val(a)
    if flag1 == True:
        break
    else:
        Flag_start = True


Flag_start = True
while Flag_start:
    b = input("Введите ширину прямоугольника: ")
    b = check_val(b)
    if flag1 == True:
        break
    else:
        Flag_start = True


print(f"Периметра прямоугольника равен {perimeter(a, b)} при длине {a} и ширине {b} ")
