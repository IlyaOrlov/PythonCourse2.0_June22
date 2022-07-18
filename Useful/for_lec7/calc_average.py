lst = [10000, 15000, 5000, 'Error', 2000]
k = 0   #кол-во чисел
summ = 0 #сумма
for i in lst:  # Первый способ
    if type(i) == int:
        summ += i
        k += 1
print(summ/k)
