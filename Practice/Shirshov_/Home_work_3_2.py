# Программу расчёта средней скорости автомобиля по введённым значениям времени и расстояния, пройденного за это время



def average_car_speed():
    return int(distance) / int(time)


def check_val(val):
    global flag1
    while val.isdecimal() == True:
        flag1 = True
        break
    else:
        print(val, "Будьте внимательнее, вводите только цифры!")
        flag1 = False


print("Программа расчёта средней скорости автомобиля по введённым значениям времени и расстояния")


Flag_start = True
while Flag_start:
    distance = input("Введите расстояние пройденное автомобилем (км): ")
    check_val(distance)
    if flag1 == True:
        break
    else:
        Flag_start = True


Flag_start = True
while Flag_start:
    time = input("Введите потраченое время (ч): ")
    check_val(time)
    if flag1 == True:
        break
    else:
        Flag_start = True


print(f"Средняя скорость автомобиля составила {round(average_car_speed(),2)}, \n"
      f"при затраченом времени {time} ч. и пройденом пути {distance} км.,\n"
      f"(!внимание результат округлен до сотых)")