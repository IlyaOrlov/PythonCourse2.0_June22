f = open("1.txt", "r")
a = input("Введите 'n' для сворачивания и 'k' для разворачивания табуляции: ")
with open("1.txt", "r") as f:
    for i in f:
        if a == "n":
            print(i.replace("\n", "    "))
        elif a == 'k':
            print(i.replace("    ", "\n"))
        else:
            print("Ошибка! Введите 0 или 1")
f.close()