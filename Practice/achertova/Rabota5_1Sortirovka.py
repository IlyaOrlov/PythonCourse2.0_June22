def ind(b, lst):
    a = 0
    for i in lst:
        if i == b:
            c = a
        break
        a += 1
    return c



lst = [4, 15, 4, 1, 999, 1000, 33, 7, 7, 1000000, 0]
for i in range(0, 10):
    for j in range(0,10):
        if lst[i] <= lst[j]:
            b = lst[i]
            a = 0
            for i in lst:
                if i == b:
                    c = a
                    print(c)
                    print(i)
                    lst[i], lst[с] = lst[c], lst[i]
                break
                a += 1

            print(lst)




# x = 0
# y = 0
# for i in lst:
#     for j in lst:
#         if i <= j:
#             lst[x], lst[y] = lst[y], lst[x]
#         y += 1
#     x += 1
#     y = 0
# print(lst)



# i = 0
# while i < len(lst):
#     lstnew = lst[i::]
#     min1 = min(lstnew)
#     indexlement = lst.index(min1)
#     lst[indexlement], lst[i] = lst[i], lst[indexlement]
#     i += 1
# print(lst)