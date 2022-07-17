import random
lst = ['камень', 'ножницы', 'бумага']
b = input("Выберите позицию")
c = random.choice(lst)
win = "Вы выиграли"
lose = "Вы проиграли"
if c == b:
    print("ничья")
if b == lst[0]:
    if c == lst[1]:
        print(win)
    elif c == lst[2]:
        print(lose)
if b == lst[1]:
    if c == lst[0]:
        print(lose)
    elif c == lst[2]:
        print(win)
if b == lst[2]:
    if c == lst[0]:
        print(win)
    elif c == lst[1]:
        print(lose)
