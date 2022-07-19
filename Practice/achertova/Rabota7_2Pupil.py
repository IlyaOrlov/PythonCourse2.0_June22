import time
import random


class Man:
	def __init__(self, n):
		self.name = n

	@staticmethod
	def solve_task():
		print(f"I'm not ready yet")


class Pupil(Man):

	@staticmethod
	def solve_task():
		time.sleep(random.randint(3, 6))
		Man.solve_task()


p1 = Pupil("Ivan")
p1.solve_task()
