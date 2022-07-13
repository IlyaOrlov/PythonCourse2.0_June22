import random


def check_guess(g):
    while not g.isdecimal() or int(g) < s1 or int(g) > s2:
        print("Будьте внимательны! Введите целое числовое значение внутри диапазона!")
        g = input("Введите значение еще раз: ")
    return g


s1 = input("Введите начало диапазона чисел: ")
while not s1.isdecimal():
    print("Введите числовое целое значение!")
    s1 = input("Введите начало диапазона чисел еще раз: ")
s1 = int(s1)
s2 = input("Введите конец диапазона чисел: ")
while not s2.isdecimal() or int(s1) >= int(s2):
    print("Числовое значение должно быть целым и большим по значению!")
    s2 = input("Введите конец диапазона чисел еще раз: ")
s2 = int(s2)
number = random.randint(s1, s2)
guess = input("Угадайте значение внутри диапазона: ")
guess = check_guess(guess)
guess = int(guess)
while guess != number:
    if guess < number:
        print("Загаданное число немного больше!")
    elif guess > number:
        print("Загаданное число немного меньше!")
    guess = input("Попробуй еще: ")
    guess = int(check_guess(guess))
else:
    print("Победа! Вы угадали!")

print(number)
