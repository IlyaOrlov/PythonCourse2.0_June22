# 1.Напишите программу, которая выводит на экран числа от 1 до 100. При этом вместо чисел, кратных трем,
# программа должна выводить слово Fizz, а вместо чисел, кратных пяти — слово Buzz. Если число кратно пятнадцати,
# то программа должна выводить слово FizzBuzz.
for gen in range(1, 101):
    if gen % 15 == 0:
        print(end=''"FizzBuzz ")
    elif gen % 3 == 0:
        print(end=''"Fizz ")
    elif gen % 5 == 0:
        print(end=''"Buzz ")
    else:
        print(gen, end=' ')
# 2.Составить программу, которая будет считывать введённое пятизначное число. После чего,
# каждую цифру этого числа необходимо вывести в новой строке:
# Число: 10819
# 1 цифра равна 1
# 2 цифра равна 0
# 3 цифра равна 8
# 4 цифра равна 1
# 5 цифра равна 9

number = input("Введите пятизначное число: ")
while len(number) != 5 or not number.isdecimal():
    number = input("Неверно. Попробуйте ещё раз: ")

for n in range(1, len(number) + 1):
    print(f"{n} цифра равна {number[n - 1]}")

# 3.Реализовать цикл, формирующий число из вводимых пользователем символов, пока не будет введено слово “stop”
# (или “Stop”, или “STOP”). Если пользователь ввел не числовой символ, вывести предупреждение и запросить новый символ.

while True:
    n = input("Введите число: ")
    if n.lower() == 'stop':
        break
    elif not n.isdecimal():
        print(f"Введены буквенные символы : {n}")
    else:
        print(f'Ваше число : {n}')

# 7.Написать декоратор, выводящий "===========" до и после запуска функции.

def dec1(fn):
    def wr():
        print('===========')
        fn()
        print('============')

    return wr


def dec2():
    print('ДЕКОРАТОР')

dec2 = dec1(dec2)
dec2()

# 8.Написать приложение – игру "камень, ножницы, бумага".


import random


while True:
    user = input("Сделайте выбор — камень, ножницы или бумага: ")
    possible_actions = ["камень", "бумага", "ножницы"]
    comp = random.choice(possible_actions)
    print(f"\nВы выбрали {user}, компьютер выбрал {comp}.\n")
    if user == comp:
        print(f"Оба игрока выбрали {user}. Ничья!!")
    elif user == "камень":
        if comp == "ножницы":
            print("Камень бьет ножницы! Вы победили!")
        else:
            print("Бумага оборачивает камень! Вы проиграли.")
    elif user == "бумага":
        if comp == "камень":
            print("Бумага оборачивает камень! Вы победили!")
        else:
            print("Ножницы режут бумагу! Вы проиграли.")
    elif user == "ножницы":
        if comp == "бумага":
            print("Ножницы режут бумагу! Вы победили!")
        else:
            print("Камень бьет ножницы! Вы проиграли.")
    pl = ""
    pl = input("С играем еще? (д/н): ")
    if pl.lower() != "д":
        break
