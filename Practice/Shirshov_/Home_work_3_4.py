print(f"Программа заменяющая все буквы “А” в слове, введённом пользователем, на символ “*”")


start = True


while start:
    s1 = input("введите строку с буквой а (En): ")
    if (s1.find("A") != -1) or (s1.find('a') != -1):
        s2 = s1.replace("a", "*").replace("A", "*")
        print(f"измененая строка получилась: {s2}")
    else:
        print(" введенной строке нет А или а ")