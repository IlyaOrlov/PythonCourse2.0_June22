s1 = input("Введите число: ")
s2 = input("Введите другое число: ")
def fun1(a, b):
    if s1 > s2 :
        print(f"Большее число - {s1}")
    elif s2 > s1 :
        print(f"Большее число - {s2}")
    else:
        print("Оба Числа равны !")

def fun2(x, y):
    if s1 > s2:
        return s1
    elif s2 > s1:
        return s2
    else:
        return s1, s2

fun1(s1, s2)
fun2(s1, s2)
