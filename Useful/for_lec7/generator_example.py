lst = [1, 2, 3, 4]
t = (i for i in lst if i % 2 != 0)
for n in t:
    print(n)
