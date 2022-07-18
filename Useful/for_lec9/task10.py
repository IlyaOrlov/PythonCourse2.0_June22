def fun(n):
    i = 0
    cnt = 0
    while cnt < n:
        yield i
        i += 2
        cnt += 1


gen = fun(3)
print(gen)
# for i in gen:
#     print(i)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))