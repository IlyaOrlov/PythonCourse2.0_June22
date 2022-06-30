# 1.Расположить инструкции программы для вычисления площади круга в правильном порядке
#
#  result = square(int(radius))
#
#  result = square(int(radius))
#
#  print(f"Площадь круга: {result}")
#
#     def square(r):
#     return math.pi * r ** 2 # Оператор def применяется после импорта
#
#  radius = input("Введите радиус: ")
#
#  import math # Импортируемые библеотеки в начале.


# Ответ:

    import math

  def square(r):
  return math.pi * r ** 2

radius = input("Введите радиус :")
result = square(int(radius))
print(f"Площадь круга {result}")

#2.
# start = input("Топлива было: "); end = input("Топлива осталось: ") # несколько операторов в одной строке (точка с запятой)
# distance = input("Расстояние: ")
# diff = int(start) - int(end)
# result = diff / distance # Не правельный расчет, целочисленный тип данных int отсутсвует.
# print # Нет переменной для вывода

#Исправлено:

start = input("Топлива было :" )
end = input("Топлива осталось :")
distance = input("Расстояние :" )
diff = int(start) - int(end)
result = (int(diff) * int(distance))/100
print(result)