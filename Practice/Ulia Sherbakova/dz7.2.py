import time
import random


class Man:

    def __init__(self, name):
        self.name = name

    @staticmethod
    def solve_task():
        print(f"I'm not ready yet.")


class Pupil(Man):

    def solve_task_n(self):
        s = random.randint(3, 6)
        time.sleep(s)
        super().solve_task()


man1 = Man("ivan")
man1.solve_task()
print(man1.name)
man2 = Pupil("Egor")
man2.solve_task_n()
print(man2.name)