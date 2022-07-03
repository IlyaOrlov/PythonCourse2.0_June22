# программа для вычисления среднего расхода бензина


flag_start = True
while flag_start:
    start = input("Введите сколько было топлива (только целые числа): ")
    try:
        val_start = int(start)
        flag_start = False
        break
    except ValueError:
        print(start, "Будьте внимательнее, вводите только цифры")


flag_end = True
while flag_end:
    end = input("Введите сколько осталось топлива (только целые числа): ")
    try:
        val_end = int(end)
        if val_end > val_start:
            print(end, "Будьте внимательнее, остатки топлива не должны превышать начальное зачение")
            flag_end = True
        else:
            break
    except ValueError:
        print(end, "Будьте внимательнее, вводите только цифры")


flag_distance = True
while flag_distance:
    distance = input("Введите длину пройденного маршрута (только целые числа): ")
    try:
        val_distance = int(distance)
        flag_distance = False
        break
    except ValueError:
        print(distance, "Будьте внимательнее, вводите только цифры")


val_diff = val_start - val_end
result = val_diff / val_distance


print(f"Средний расход составил: {round(result,2)} *(результат округлен до сотых)")   # вывод на экран
