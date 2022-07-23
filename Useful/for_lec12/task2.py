import random
import time


def compute(number):
    # что-то долго вычисляем
    print(f'Старт вычислений №{number}')
    sleeping = random.randint(1, 5)
    time.sleep(sleeping)
    print(f'Конец вычислений №{number}. Затрачено {sleeping} секунд')

start = time.perf_counter()
# считаем что-то много раз с разными параметрами
for i in range(5):
    compute(i)
print(f'Общее время вычислений в секундах: {int(time.perf_counter() - start)}')
