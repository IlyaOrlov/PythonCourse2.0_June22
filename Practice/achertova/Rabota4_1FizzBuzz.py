a = 1
while a <= 100:
    if a % 3 == 0 and a % 5 != 0:
        print(f"Fizz")
    elif a % 3 != 0 and a % 5 == 0:
        print(f"Buzz")
    elif a % 3 == 0 and a % 5 == 0:
        print(f"FizzBuzz")
    else:
        print(a)
    a += 1
