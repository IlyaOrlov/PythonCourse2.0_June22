def fun(arr):
    dup = []
    uniq = []
    for i in arr:
        if i in uniq:
            dup.append(i)
        else:
            uniq.append(i)
    print(dup[0])


arr = [2, 3, 4, 5, 3, 2]
fun(arr)