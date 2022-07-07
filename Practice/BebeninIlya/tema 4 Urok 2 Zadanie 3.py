while (s := len(input("Введите что-нибудь "))):
    if s == s.isdecimal(s):
        print(f"Ваше число {s}")
    else:
        s = "Stop"
        break