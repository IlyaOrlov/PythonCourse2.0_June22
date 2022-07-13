a = 1
while a <= 100:
    if a % 15 == 0:
        print(f"FizzBuzz")
    elif a % 3 == 0:
        print(f"Fizz")
    elif a % 5 == 0:
        print(f"Buzz")
    else:
        print(a)
    a += 1
