key = 198104
a = input("Введите пароль: ")
p = 12345

while not int(a) == int(p):
    print("Введите правильный пароль ")
    a = input("Введите пароль: ")
res = p ^ key
print(f"Ваш ключ: {res}")

res1 = res ^ key
print(res1)

