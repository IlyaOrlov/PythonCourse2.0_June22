import random
lst = ['камень', 'ножницы', 'бумага']
b = input("Выберите позицию")
c = random.choice(lst)
win = "Вы выиграли"
lose = "Вы проиграли"
if c == b:
    print("ничья")
elif b == lst[0]:
    if c == lst[1]:
        print(win)
    else:
        print(lose)
elif b == lst[1]:
    if c == lst[0]:
        print(lose)
    else:
        print(win)
elif b == lst[2]:
    if c == lst[0]:
        print(win)
    else:
        print(lose)
