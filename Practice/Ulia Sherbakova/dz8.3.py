import time


class TestManager:
    def __enter__(self):
        print('Starting code.')
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Code completed.')


with TestManager():
    startTime = time.time()
    s = 'строкадлязаменысимволов'
    x = {'а': 3, 'з': 5, 'о': 7}
    for key in x.keys():
        s = s.replace(key, str(x[key]))
    print(s)
    endTime = time.time()
    totalTime = endTime - startTime
    print("Время, затраченное на выполнение данного кода = ", totalTime)