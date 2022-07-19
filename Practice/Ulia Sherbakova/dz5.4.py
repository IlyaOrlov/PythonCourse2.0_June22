import numpy as np

def fun(arr):
    a = 9
    s = len(arr)
    c = 0
    new = []
    while c < s - 1:
        for i in arr:
            for j in i:
                if j == a:
                    new.append(i)
                    print(new)
                    np.delete(arr, new, 0)
        c += 1
    print(arr)



arr = [[1, 5, 8], [7, 2, 9], [4, 3, 1]]
fun(arr)
