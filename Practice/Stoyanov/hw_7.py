'''1. Написать класс Man, который принимает имя в конструкторе. Имеет метод solve_task, который просто выводит
"I'm not ready yet".
'''

# class Man:
#
#     def __init__(self, name):
#         self.name = name
#
#     @staticmethod
#     def solve_task():
#         print("I'm not ready yet.")
#
#
# name_0 = input("Введите ваше имя: ")
# m = Man(name_0)
# m.solve_task()

'''2. Написать класс Pupil, у которого переопределен метод solve_task. На этот раз он будет думать от 3 до 6 секунд 
(c помощью метода sleep библиотеки time и randint библиотеки random).
'''
# from time import sleep
# from random import randint
#
#
# class Pupil(Man):
#
#     def solve_task(self):
#         print(f"{self.name} думает...")
#         sleep(randint(3, 6))
#         super().solve_task()
#
#
# name_1 = input("Введите ваше имя: ")
# p_1 = Pupil(name_1)
# p_1.solve_task()
#
# name_2 = input("Введите ваше имя: ")
# p_2 = Pupil(name_2)
# p_2.solve_task()

"""3.* Реализовать систему, эмулирующую работу с банкоматами. Создать семейство классов банкоматов, 
хранящих определенные суммы и поддерживающих различные операции (одни банкоматы принимают и выдают наличные, 
другие позволяют еще и проводить онлайн платежи). Операции реализуются посредством методов, выводящих название 
операции и меняющих (при необходимости) количество наличных в банкомате. Для тестирования системы необходимо 
реализовать алгоритм, обходящий список банкоматов разного типа и запрашивающий у каждого банкомата информацию о 
количестве наличных и наборе поддерживаемых операций.
"""

class Bancomat_old:

    def __init__(self, cash):
        self.cash = cash
        print(f"Банкомат создан, его баланс {self.cash}p")

    def balance(self):
        print(f"Баланс = {self.cash}")
        print("-" * 10)

    def put_money(self, money):
        if money > 0:
            self.cash += money
            print(f"Вы внесли {money}р")
        else:
            print("Ошибка! Сумма должна быть больше 0!")

    def give_money(self, money):
        if self.cash - money > 0:
            self.cash -= money
            print(f"Вы сняли {money}р")
        else:
            print(f"Недостаточно средств! В банкомате всего {self.cash}")

    def online(self, money):
        print("Данный банкомат не умеет совершать онлайн платежи!")

    def info(self):
        print(f"Баланс банкомата - {self.cash}\nБанкомат умеет только принимать и выдавать деньги.")
        print("-" * 10)

class Bancomat_new(Bancomat_old):

    def online(self, money):
        if self.cash - money > 0:
            self.cash -= money
            print(f"Вы совершили онлайн платеж на {money}р")
        else:
            print("Недостаточно средств!")

    def info(self):
        print(f"Баланс банкомата - {self.cash}\nБанкомат умеет принимать, выдавать деньги и совершать онлайн платежи.")
        print("-"*10)

b1 = Bancomat_old(1000)
b1.put_money(589)
b1.balance()
b2 = Bancomat_old(2000)
b2.give_money(1340)
b2.balance()
b3 = Bancomat_old(15000)
b3.online(200)
b3.balance()
nb1 = Bancomat_new(9000)
nb1.online(50)
nb1.balance()
nb2 = Bancomat_new(1000)
nb2.give_money(700)
nb2.balance()

lst = [b1, nb2, b2, b3, nb1]
for i in lst:
    i.info()

