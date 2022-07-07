s = input("Введите пятизначное число: ")
if len(s) == 5:
    for i in s:
        i = int(i)
        print(f'{i}  цифра равна = {i}')

else:
    print ("Введено неправильное значение")