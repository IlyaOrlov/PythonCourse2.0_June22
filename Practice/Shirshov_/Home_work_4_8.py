#игра "камень, ножницы, бумага".


import random
def check_val(val):
    while True:
        res = input(val)
        if res.lower() == 'стоп':
            return False
        else:
            if res.isdecimal():
                res = int(res)
                if res == 2 or res == 4 or res == 6:
                    return res
                else:
                    print(res, "Будьте внимательнее, не забывайте правила игры [2], [4] или [6]")
            else:
                print(res, "Вводите только цифры.")


def result(mes):
    if mes == 2:
        return "камень"
    elif mes == 4:
        return "ножницы"
    else:
        return "бумага"


print("Игра -'камень, ножницы, бумага'")
print('\n Условие игры: вам необходимо задать число в соответствии с вашим выбором:\n   [2]- это камень \n'
      '   [4]- это ножницы \n   [6]- это бумага \n Чтобы закончить наберите слово "стоп"\n')


n1 = [2, 4, 6]


while True:
    user = check_val('Введите ваш вариант: ')
    if user == False:
        print('Игра остановлена пользователем.')
        break
    else:
        comp = int(random.choice(n1))
        print(f'Ваш вариант: "{result(user)}"         Вариант робота Алисы: "{result(comp)}"')
        # print(comp) # только для отладки программы
        if result(user) == result(comp):
            print(" Ничья !!!")
        elif user == 2 and comp != 6:
            print("Ура вы победили!!!!!")
        elif user == 4 and comp != 2:
            print("Ура вы победили!!!!!")
        elif user == 6 and comp != 4:
            print("Ура вы победили!!!!!")
        else:
            print('  К сожалению вы проиграли.\n  Не отчаивайся, попробуй еще раз.')
        print('===============================')
print('################ THE END #######################')
