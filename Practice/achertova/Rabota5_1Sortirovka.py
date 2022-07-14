lst = [4, 15, 1, 999, 1000, 33]
i = 0
while i < len(lst):
    lstnew = lst[i::]
    min1 = min(lstnew)
    indexlement = lst.index(min1)
    lst[indexlement], lst[i] = lst[i], lst[indexlement]
    i += 1
print(lst)
