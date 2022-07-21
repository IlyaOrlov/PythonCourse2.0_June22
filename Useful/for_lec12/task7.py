import multiprocessing
import time


def count(n):
    while n > 0:
        n -= 1


if __name__ == '__main__':  # обязательно для многопроцессного приложения
    c = 80000000
    start = time.perf_counter()
    p1 = multiprocessing.Process(target=count, args=(c,))
    p2 = multiprocessing.Process(target=count, args=(c,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(f'{time.perf_counter() - start:.2f} sec.')
