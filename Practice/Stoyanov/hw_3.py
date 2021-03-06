'''1. Написать программу для расчёта периметра прямоугольника по введённым длине и ширине.'''

def area(a, b):
    return 2*(a + b)


if __name__ == '__main__':
    length = int(input("Длина прямоугольника: "))
    width = int(input("Ширина прямоугольника: "))
    result = area(length, width)
    print(f"Периметр прямоугольника = {result}")

"""2. Написать программу для расчёта средней скорости автомобиля по введённым значениям времени и расстояния, 
пройденного за это время."""

def speed(d, t):
    return d/t


if __name__ == '__main__':
    distance = int(input("Сколько километров пройдено: "))
    time = int(input("Сколько часов затрачено: "))
    result = speed(distance, time)
    print(f"Средняя скорость автомобиля была: {result}км/ч")

'''3. Написать две программы: одна должна шифровать введённый пользователем цифровой пароль при помощи секретного 
кода, другая – расшифровывать получившийся результат при помощи ЭТОГО ЖЕ секретного кода.'''

word = int(input("Введите ваш пароль, состоящий из цифр: "))
key = 987415
encode = word ^ key
decode = encode ^ key
print(f"Ваш пароль - {word}, зашифрованный пароль - {encode}, расшифрованный пароль - {decode}")

'''4. Написать программу, заменяющую все буквы “А” в слове, введённом пользователем, на символ “*”.'''

word = input("Введите слово: ")
word_new = word.replace("A", "*")
print(word_new)

'''5. Написать программу, проверяющую, что слово, введённое пользователем, является палиндромом (примеры: “Топот”, 
“Довод”). Программа должна выводить True или False'''

word = input("Введите слово для проверки на пaлиндром: ").lower()
if word == word[::-1]:
    print("True")
else:
    print("False")
