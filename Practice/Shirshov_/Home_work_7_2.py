# Написать класс Pupil, у которого переопределен метод solve_task.
# На этот раз он будет думать от 3 до 6 секунд (c помощью метода sleep библиотеки time и randint библиотеки random).
import time
import random


class Man:
    def __init__(self, name):
        self.man_name = name

    @staticmethod
    def solve_task():
        print("I'm not ready yet")


class Pupil(Man):

    @staticmethod
    def solve_task(mes1, mes2):
        sek = random.randint(mes1, mes2)
        #print(f"{time.sleep(sek)} I'm not ready yet")
        (time.sleep(sek)), print(f"I'm not ready yet")


men1 = Man("Rembo")
men2 = Pupil("Tom")

men1.solve_task()
men2.solve_task(3, 6)
