import random

beg = int(input("Введите нижнюю границу диапазона: "))
end = int(input("Введите верхнюю границу диапазона: "))
while end < beg or end == beg:
    print(f"Верхняя граница должна быть больше нижней")
    break
random = random.randint(beg, end)
while (s := input("Угадай число из этого диапазона: ")).isdecimal():
    if int(s) > random:
        print(f"Число немного меньше {s}")
    elif int(s) < random:
        print(f"Число немного больше {s}")
    elif int(s) == random:
        print(f"Поздравляю, вы угадали")
        break
