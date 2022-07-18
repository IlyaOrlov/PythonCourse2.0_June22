'''1. Написать класс Man, который принимает имя в конструкторе. Имеет метод solve_task, который просто выводит
"I'm not ready yet".
'''

class Man:

    def __init__(self, name):
        self.name = name

    @staticmethod
    def solve_task():
        print("I'm not ready yet.")


name = input("Введите ваше имя: ")
m = Man(name)
print(m.name)
m.solve_task()

'''2. Написать класс Pupil, у которого переопределен метод solve_task. На этот раз он будет думать от 3 до 6 секунд 
(c помощью метода sleep библиотеки time и randint библиотеки random).
'''
from time import sleep
from random import randint


class Pupil(Man):

    def __init__(self, name):
        super().__init__(name)
        self.name = name

    def solve_task(self):
        print(f"{name} думает...")
        sleep(randint(3, 6))
        super().solve_task()


name = input("Введите ваше имя: ")
p = Pupil(name)
p.solve_task()
