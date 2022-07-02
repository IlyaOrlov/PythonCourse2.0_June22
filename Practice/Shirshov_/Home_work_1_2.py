print("Новая задача")

import time


def fun(x, y):
    return x + y


start = time.time()
x = input("Веедите первое слогаемое: ")
y = input("Введите второе слогаемое: ")
result = fun(int(x), int(y))
passed = time.time() - start
print(f"Сумма = {result}")
print(f"Затраченное время {passed}  секунд")
print("the END")
