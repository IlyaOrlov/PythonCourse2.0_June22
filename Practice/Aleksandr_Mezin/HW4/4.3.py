import random

while True:
    s = input("Введите число: ")
    if s.lower() == 'stop':
        break
    elif not s.isdecimal():
        print("Нужно ввести число")
    else:
        s1 = random.choice(s)
        print(s1)
