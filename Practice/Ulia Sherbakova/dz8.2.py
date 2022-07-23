def fun():
    with open("1.txt", "r") as file:
        for line in file:
            yield line


f = fun()
print(next(f))
print(next(f))
print(next(f))
