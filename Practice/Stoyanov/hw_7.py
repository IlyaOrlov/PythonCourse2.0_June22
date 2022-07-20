'''1. Написать класс Man, который принимает имя в конструкторе. Имеет метод solve_task, который просто выводит
"I'm not ready yet".
'''

class Man:

    def __init__(self, name):
        self.name = name

    @staticmethod
    def solve_task():
        print("I'm not ready yet.")


name_0 = input("Введите ваше имя: ")
m = Man(name_0)
m.solve_task()

'''2. Написать класс Pupil, у которого переопределен метод solve_task. На этот раз он будет думать от 3 до 6 секунд 
(c помощью метода sleep библиотеки time и randint библиотеки random).
'''
from time import sleep
from random import randint


class Pupil(Man):

    def solve_task(self):
        print(f"{self.name} думает...")
        sleep(randint(3, 6))
        super().solve_task()


name_1 = input("Введите ваше имя: ")
p_1 = Pupil(name_1)
p_1.solve_task()

name_2 = input("Введите ваше имя: ")
p_2 = Pupil(name_2)
p_2.solve_task()