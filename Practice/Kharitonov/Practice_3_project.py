# 1.Написать программу для расчёта периметра прямоугольника по введённым длине и ширине.
# import pycryptodome as pycryptodome
#
len = float(input("Введите длину прямоугольника (см) :"))
wid = float(input("Введите ширину прямоугольника (см) :"))
per = (len + wid) * 2
print(f"S = {per} см.")
#
# 2.Написать программу для расчёта средней скорости автомобиля по введённым значениям времени и расстояния, пройденного
# за это время.
tim = float(input("Введите врямя (час.) :"))
dist = float(input("Введите растояние (км.) :"))
V = dist / tim
print(f"Средняя скорость = {V}")
#
#4.Написать программу, заменяющую все буквы “А” в слове, введённом пользователем, на символ “*”.
#
text = input("Слово :")
print(f"Маскирование : {text.replace('А', '*').replace('а', '*').replace('A', '*').replace('a', '*')}")
