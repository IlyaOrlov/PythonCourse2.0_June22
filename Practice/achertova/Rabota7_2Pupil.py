import time
import random


class Pupil:
	def __init__(self, n):
		self.name = n

	@staticmethod
	def solve_task():
		time.sleep(random.randint(3, 6))
		print(f"I'm not ready yet")


p1 = Pupil("Ivan")
p1.solve_task()
