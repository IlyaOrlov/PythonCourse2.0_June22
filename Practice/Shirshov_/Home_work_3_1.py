# Программа для расчёта периметра прямоугольника по введённым длине и ширине


def perimeter(a, b):
    return (int(a) + int(b)) * 2


def check_val(mes):
    while True:
        val = input(mes)
        if val.isdecimal():
            return val
        else:
            print(val, "Будьте внимательнее, вводите только цифры!")
            True


if __name__ == '__main__':
    print("Программа для расчёта периметра прямоугольника")
    a = check_val("Введите длину прямоугольника: ")
    b = check_val("Введите ширину прямоугольника: ")
    print(f"Периметра прямоугольника равен {perimeter(a, b)} при длине {a} и ширине {b} ")
