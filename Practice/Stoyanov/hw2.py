"""Задание 1. Расположить инструкции программы для вычисления площади круга в правильном порядке."""
import math


def square(r):
    return math.pi * r ** 2


if __name__ == '__main__':
    radius = input("Введите радиус: ")
    result = square(int(radius))
    print(f"Площадь круга: {result}")

"""Задание 2. Следующая программа для вычисления среднего расхода бензина содержит различные ошибки. Необходимо их 
найти и исправить."""

start = input("Топлива было: ")
end = input("Топлива осталось: ")
distance = input("Расстояние: ")
diff = int(start) - int(end)
result = int(diff) / int(distance)
print(f"Всего было затрачено {diff} топлива, средний расход топлива составил {result}л.")
