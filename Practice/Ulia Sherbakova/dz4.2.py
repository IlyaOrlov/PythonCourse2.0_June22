s = input("Введите пятизначное число: ")
if len(s) == 5:
    print(f"1 цифра равна {s[0]}")
    print(f"2 цифра равна {s[1]}")
    print(f"3 цифра равна {s[2]}")
    print(f"4 цифра равна {s[3]}")
    print(f"5 цифра равна {s[4]}")
else:
    print("Я просил пятизначное")