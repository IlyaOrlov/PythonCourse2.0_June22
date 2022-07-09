key = 12345
a = input("Введите ключ: ")
p = 1765464

while not int(key) == int(a):
    print("Введите корректный ключ ")
    a = input("Введите ключ: ")

res = p ^ key
print(f"Ваш токен, {res}")
b = input("Введите токен ")

while not int(res) == int(b):
    print("Неверный токен:")
    b = input("Введите токен: ")

res1 = res ^ key
print(res1)
