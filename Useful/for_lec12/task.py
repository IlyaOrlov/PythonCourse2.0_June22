import multiprocessing


status = 'Not ready'


def fun():
    global status
    print(f'{__name__}: {status = }')
    status = 'Ready'
    print(f'{__name__}: {status = }')


if __name__ == '__main__':
    t = multiprocessing.Process(target=fun)
    t.start()
    t.join()
    print(f'{__name__}: {status = }')