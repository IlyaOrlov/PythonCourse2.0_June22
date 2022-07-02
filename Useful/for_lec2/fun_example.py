def fun(lst):
    lst.append(100)


a = [1, 2, 3]
b = [1, 2, 3]

print(f"{id(a)=}")
print(f"{id(b)=}")

fun(a)
print(f"{a=}")
print(f"{b=}")