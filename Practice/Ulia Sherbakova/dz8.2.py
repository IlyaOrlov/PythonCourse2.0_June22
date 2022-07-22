def fun():
    file = open("1.txt", 'r')
    for line in file:
        yield line
    file.close()


f = fun()
print(next(f))
print(next(f))
print(next(f))
