a = 10
b = a
a = "hello"
print(f"{id(a)=}")  # "hello"
print(f"{id(b)=}")  # 10
