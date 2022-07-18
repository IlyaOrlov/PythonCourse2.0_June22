def gen_fun():
    print("begin")
    for i in [1, 2]:
        print("before yield", i)
        yield i
        print("after yield", i)
    print("end")


f = gen_fun()
print(f)
print(next(f))
print('------')
print(next(f))
print('------')
print(next(f))