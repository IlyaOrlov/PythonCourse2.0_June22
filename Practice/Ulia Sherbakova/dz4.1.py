for n in range(1,101):
    if n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    elif n % 15 == 0:
        print("FizzBuzz")
    else:
        print(n)