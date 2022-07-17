import random

print("введи начало диапазона:")
start = input()
print("введи конец диапазона:")
stop = input()
random_number = random.randint(int(start) - 1, int(stop) + 1)
print(random_number)
while True:
    print("введи число которое я загадал!")
    number = input()
    if number.isdigit() == False:
        print("Вводить нужно число!")

    else:
        number = int(number)
        if number == random_number:
            print("молодец! угадал :)")
            break

        elif number < random_number:
            print("число больше")

        elif number > random_number:
            print("число меньше")