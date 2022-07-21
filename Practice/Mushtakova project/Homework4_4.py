import random

b = ("И?", "Ты сам-то понял, что написал?", "Аргументируй?")
while (a := input("Задай вопрос: ")) != "хватит":
    print(random.choice(b))

