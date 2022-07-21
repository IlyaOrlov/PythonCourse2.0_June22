import threading
import random
import time


def compute(number):
    # что-то долго вычисляем тем же способом
    print(f'Старт вычислений №{number}')
    sleeping = random.randint(1, 5)
    time.sleep(sleeping)
    print(f'Конец вычислений №{number}. Затрачено {sleeping} секунд')

start = time.perf_counter() # считаем что-то много раз с разными параметрами
threads = []
for i in range(5):
    thr = threading.Thread(target=compute, args=(i,))
    thr.start()
    threads.append(thr)

for thr in threads:
    thr.join()
print(f'Общее время вычислений в секундах: {int(time.perf_counter() - start)}')
