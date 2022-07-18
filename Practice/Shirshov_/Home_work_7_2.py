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

    def solve_task_new(self):
        return time.sleep(random.randint(3, 6)), super().solve_task()


men1 = Man("Rembo")
men2 = Pupil("Tom")


men1.solve_task()
men2.solve_task_new()
