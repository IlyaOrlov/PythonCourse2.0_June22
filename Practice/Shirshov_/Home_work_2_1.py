import math   # импорт библиотеки


def square(r):   # определение функции
    return math.pi * r ** 2


radius = input("Введите радиус: ")   # ввод исходных данных
result = square(int(radius))         #подготовка результата к выводу

print(f"Площадь круга: {result}")    #вывод на экран