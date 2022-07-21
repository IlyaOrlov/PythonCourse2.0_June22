def change(f, a, b):
    for s in f:
        s.replace(a, b)
        print(s)


f = open("1.txt", "r")
while (request := input("Заменить табуляцию - ввод tab, заменить пробелы - ввод space:")) not in {"tab", "space"}:
    print("Ошибка ввода!")
if request == "tab":
    change(f, "/t", "    ")
else:
    change(f, "    ", "/t")
f.close()

    #не работает, а в файле tab выглядит как пробел. В настройках что-то боюсь менять :(
