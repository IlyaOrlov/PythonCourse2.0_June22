import random


while (s := input("Ваш ход. Для выхода введите stop: ")) != "stop":
    s = s.lower()
    word = ["камень", "ножницы", "бумага"]
    s2 = random.choice(word)
    if s == "камень" and s2 == "ножницы":
        print("У меня ножницы, ты победил")
    elif s == "камень" and s2 == "бумага":
        s = input("У меня бумага, я победил")
    elif s == "ножницы" and s2 == "камень":
        s = input("У меня камень, я победил")
    elif s == "ножницы" and s2 == "бумага":
        s = input("У меня бумага, я проиграл")
    elif s == "бумага" and s2 == "камень":
        s = input("У меня бумага, я победил")
    elif s == "бумага" and s2 == "ножницы":
        print("У меня ножницы, я проиграл")
    elif s == s2:
        print("Ничья! У меня такой же вариант")
    else:
        print("Проверь что написал, нужно камень/ножницы/бумага")