import random

lst = ["Ты сам-то понял, что написал?", "Аргументируй", "И?"]

while True:
    s = input("Поговорим?: ")
    if s.lower() == "хватит":
        break
    else:
        s1 = random.choice(lst)
        print(s1)
