print(f' Программа, которая считывает введённое пятизначное число.\n '
      f'После чего, каждую цифру этого числа будет выводить в новой строке.\n')


while True:
    n = input('введите пятизначное число: ')
    if n.isdecimal() and len(n) == 5:
        for i in range(1, len(n)+1):
            print(f'{i} цифра равна {n[i-1]}')
        print("########### THE END ##############")
        break
    else:
        print('Пожалуйста, внимательнее - "пятизначное число"')