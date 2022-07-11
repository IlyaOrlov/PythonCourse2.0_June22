import random

beg = int(input("Введите нижнюю границу диапазона: "))
end = int(input("Введите верхнюю границу диапазона: "))
while end < beg or end == beg:
    end = int(input("Верхняя граница должна быть больше нижней: "))
rand = random.randint(beg, end)
while (s := input("Угадай число из этого диапазона: ")).isdecimal():
    s = int(s)
    if s > rand:
        print(f"Число немного меньше {s}")
    elif s < rand:
        print(f"Число немного больше {s}")
    elif s == rand:
        print(f"Поздравляю, вы угадали")
        break
