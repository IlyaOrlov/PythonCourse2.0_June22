import time
import threading


def count(n):
    while n > 0:
        n -= 1


c = 80000000
start = time.perf_counter()
# tr_1 = threading.Thread(target=count, args=(c,))
# tr_2 = threading.Thread(target=count, args=(c,))
# tr_1.start()
# tr_2.start()
count(c)
count(c)
# tr_1.join()
# tr_2.join()

print(f'{time.perf_counter() - start:.2f} sec.')
