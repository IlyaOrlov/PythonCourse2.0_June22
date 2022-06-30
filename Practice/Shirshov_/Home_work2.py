import time
from turtledemo.penrose import star

print("Новая задача")

def fun(x, y):
    return x + y


#if  _name_ == "main":
start = time.time()
x = input("Веедите первое слогаемое: ")
y = input("Введите второе слогаемое: ")
result = fun(int(x), int(y))
passed = time.time() - start
print(f"Сумма = {result}")
print(f"Затраченное время {passed}  секунд")
