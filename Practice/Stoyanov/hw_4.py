"""1. Напишите программу, которая выводит на экран числа от 1 до 100. При этом вместо чисел, кратных трем,
программа должна выводить слово Fizz, а вместо чисел, кратных пяти — слово Buzz. Если число кратно пятнадцати,
то программа должна выводить слово FizzBuzz."""

for i in range(1, 101):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

'''2. Составить программу, которая будет считывать введённое пятизначное число. После чего, каждую цифру этого числа 
необходимо вывести в новой строке:
Число: 10819
1 цифра равна 1
2 цифра равна 0
3 цифра равна 8
4 цифра равна 1
5 цифра равна 9'''

num = input("Введите пятизначное число: ")
for i in range(1, 6):
    print(f"{i} цифра равна {num[i-1]}")
    i += 1

'''3. Реализовать цикл, формирующий число из вводимых пользователем символов, пока не будет введено слово “stop” (или 
“Stop”, или “STOP”). Если пользователь ввел не числовой символ, вывести предупреждение и запросить новый символ. '''

while True:
    word = input("Напишите что-то: ")
    if word.lower() == 'stop':
        break
    elif not word.isdecimal():
        print("Так не пойдет. Пиши только цифры!")
    else:
        print(len(word))

'''4. Написать приложение-спорщик (генератор ответов), отвечающее на все запросы пользователя последовательно 
фразами: "Ты сам-то понял, что написал?", "Аргументируй", "И?", пока пользователь не введёт слово “хватит”.'''

tuple_phrase = ("Ты сам-то понял, что написал?", "Аргументируй", "И?")
phrase = input("Что скажешь?: ")
for i in tuple_phrase:
    print(i)
    word = input("Твой ход: ")
    if word.lower() == "хватит":
        break

'''5. Реализовать приложение, загадывающее целое число из заданного пользователем диапазона и предлагающее 
пользователю это число угадать. Отгадывание числа должно быть реализовано в цикле: пока пользователь не угадает, 
или не введет нечисловой символ, продолжать опрос. Если пользователь вводит неправильное число, вывести подсказку: 
больше оно или меньше загаданного. '''

import random

interval_min = int(input("Нужно задать интервал. Введи минимальное число: "))
interval_max = int(input("Введи максимальное число: "))
number = random.randint(interval_min, interval_max)
player = input("Теперь попробуй отгадать число из заданного тобой интервала: ")
while True:
    if not player.isdecimal():
        print("Писать можно только цифры!")
        break
    player = int(player)
    if player == number:
        print("Молодец! Ты угадал.")
        break
    else:
        if player > number:
            print(f"{player} больше загаданного мною числа.")
        else:
            print(f"{player} меньше загаданного мною числа.")
    player = input("Попробуй еще раз: ")

'''6. Написать и вызвать две функции, принимающие два числа. Первая функция должна вывести на экран большее из двух 
введённых чисел. Другая должна вернуть большее из двух введённых чисел по месту вызова. '''

def fun_1(a, b):
    print(max(a, b))


def fun_2(a, b):
    return max(a, b)


fun_1(14, 67)
print(fun_2(14, 67))

'''7. Написать декоратор, выводящий "===========" до и после запуска функции.'''

def dekor(f):
    def wrapper(*args, **kwargs):
        print("===========")
        dek = f(*args, **kwargs)
        print("===========")
        return dek
    return wrapper


@dekor
def fun():
    print("Мой первый декоратор! :D")


fun()

'''8. Написать приложение – игру "камень, ножницы, бумага".'''

import random

lst = ("камень", "ножницы", "бумага")
while True:
    player = input("Что выберешь? ").lower()
    comp = random.choice(lst)
    if player == "стоп":
        break
    elif player not in lst:
        print("Пиши грамотно, я ограничен в ответах.")
    elif player == comp:
        print(f"Ничья ты выбрал '{player}' и я '{comp}'")
    elif player == "камень" and comp == "ножницы":
        print(f"Ты победил! Ты выбрал - '{player}' а я - '{comp}'")
    elif player == "ножницы" and comp == "бумага":
        print(f"Ты победил! Ты выбрал - '{player}' а я - '{comp}'")
    elif player == "бумага" and comp == "камень":
        print(f"Ты победил! Ты выбрал - '{player}' а я - '{comp}'")
    else:
        print(f"Ты проиграл! Ты выбрал - '{player}' а я - '{comp}'")
