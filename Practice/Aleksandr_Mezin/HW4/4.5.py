import random

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
i = range(a, b)
c = (random.choice(i))
a1 = input("Угадатайте число: ")
while a1.isdecimal():
    if int(a1) == c:
        print("Поздравляю Вы угадали!! ")
        break
    elif int(a1) <= c:
        print("нет, число чуть больше")
    elif int(a1) >= c:
        print("нет, число чуть меньше")
    else:
        break
    a1 = input("Угадатайте снова: ")
