def fun(arr):
    a = set()
    for i in arr:
        if i in a:
            print(i)
            break
        else:
            a.add(i)



arr = [2, 3, 4, 5, 3, 2]
fun(arr)