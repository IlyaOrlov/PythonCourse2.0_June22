import time
import random

class Man:
    def __init__(self, name):
        self.name = name

    def solve_task(self):
        print(f"I'm not ready yet.")

class Pupil(Man):
    s = random.randint(3, 6)
    time.sleep(s)

man1 = Man("ivan")
man1.solve_task()
print(man1.name)
man2 = Pupil("Egor")
man2.solve_task()
print(man2.name)