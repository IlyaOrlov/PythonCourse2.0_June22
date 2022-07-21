lst = [4, 15, 4, 1, 999, 1000, 33]
x = 0
y = 0
for i in lst:
    for j in lst:
        if i >= j:
            lst[x], lst[y] = lst[y], lst[x]
            print(lst)
        print(x, y)
        y += 1
    x += 1
print(lst)


# i = 0
# while i < len(lst):
#     lstnew = lst[i::]
#     min1 = min(lstnew)
#     indexlement = lst.index(min1)
#     lst[indexlement], lst[i] = lst[i], lst[indexlement]
#     i += 1
# print(lst)