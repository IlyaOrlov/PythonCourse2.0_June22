import threading


status = 'Not ready'


def fun():
    global status
    print(f'---- {status=}')
    status = 'Ready'
    print(f'---- {status=}')


if __name__ == '__main__':
    print(f'{__name__}: {status = }')
    t = threading.Thread(target=fun)
    t.start()
    t.join()
    print(f'{__name__}: {status = }')