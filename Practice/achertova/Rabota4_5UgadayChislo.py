import random

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
while not guess.isdecimal() or int(guess) <= s1 or int(guess) >= s2:
    print("Будьте внимательны! Введите целое числовое значение внутри диапазона!")
    guess = input("Введите значение еще раз: ")
#Хотелось бы связать этот блок и 26 строку, но как-то не родилось, поэтому посчитала, что пользователь уже научился
guess = int(guess)
while guess != number:
    if guess < number:
        print("Загаданное число немного больше!")
    elif guess > number:
        print("Загаданное число немного меньше!")
    guess = int(input("Попробуй еще: "))
else:
    print("Победа! Вы угадали!")

print(number)
