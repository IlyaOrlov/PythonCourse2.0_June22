start = input("Топлива было: ")#Программа для вычисления среднего расхода бензина
end = input("Топлива осталось: ")
distance = input("Расстояние: ")
diff = int(start) - int(end)
result = int(diff) / int(distance)
print(f"Расход бензина: {result}")