a = input("Введите 't' для сворачивания и 'k' для разворачивания табуляции: ")

with open("1.txt", "r") as f1, open("2.txt", "w") as f2:
    for i in f1:
        if a == 't':
            s = repr(i.replace("\t", "    "))
            f2.write(s)
        elif a == 'k':
            s = repr(i.replace("    ", "\t"))
            f2.write(s)
        else:
            print("Ошибка! Введите 't' или 'k'")
