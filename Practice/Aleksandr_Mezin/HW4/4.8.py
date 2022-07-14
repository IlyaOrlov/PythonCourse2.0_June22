import random
lst = ['камень', 'ножницы', 'бумага']
b = input("Выберите позицию")
c = random.choice(lst)
if  c == b:
    print("ничья")
elif b == lst[0] and c == lst[1]:
    print("Вы проиграли")
elif b == lst[0] and c == lst[2]:
    print("Вы проиграли")
elif b == lst[1] and c == lst[0]:
    print("Вы проиграли")
elif b == lst[1] and c == lst[2]:
    print("Вы выиграли")
elif b == lst[2] and c == lst[0]:
    print("Вы выиграли")
elif b == lst[2] and c == lst[1]:
    print("Вы проиграли")
