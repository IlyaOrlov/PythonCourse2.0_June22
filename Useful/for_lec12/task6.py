import gevent
import time

def count(n):
    while n > 0:
        n -= 1

c = 80000000
start = time.perf_counter()
g1 = gevent.spawn(count, c) # создаем и запускаем 1-й гринлет
g2 = gevent.spawn(count, c) # создаем и запускаем 2-й гринлет
gevent.joinall([g1, g2]) # ожидаем завершения гринлета
print(f'{time.perf_counter() - start:.2f} sec.')
