#первая программа

kod = 123
s = input("Введите цифровой пароль: ")
shif = int(s) ^ kod
print(f"Шифрование: {shif}")

#вторая программа

deshif = shif ^ kod
print(f"Расшифровка: {deshif}")