#программа для вычисления среднего расхода бензина

start = int(input("Топлива было: "))    # ввод исходных данных
end = int(input("Топлива осталось: "))  # ввод исходных данных
distance = int(input("Расстояние: "))  # ввод исходных данных


diff = start - end
result = diff / distance


print(f"Средний расход бензина составляет: {result}")   # вывод на экран