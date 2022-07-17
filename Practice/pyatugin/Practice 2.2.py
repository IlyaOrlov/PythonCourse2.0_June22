start = input("Топлива было: "); end = input("Топлива осталось: ")#Программа для вычисления среднего расхода бензина
distance = input("Расстояние: ")
diff = int(start) - int(end)
result = int(diff) / int(distance)
print(f"Расход бензина: {result}")