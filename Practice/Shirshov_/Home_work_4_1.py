# Программа, которая выводит на экран числа от 1 до 100.
# При этом вместо чисел, кратных трем, программа должна выводить слово Fizz,
# а вместо чисел, кратных пяти — слово Buzz. Если число кратно пятнадцати,
# то программа должна выводить слово FizzBuzz.


n = int(input('введите конечное число: '))


for i in range(1, n+1):
    st = i
    if st % 3 == 0:
        i = 'Fizz'
    if st % 5 == 0:
         i = 'Buzz'
    if st % 15 == 0:
        i = 'FizzBuzz'

    print(i)