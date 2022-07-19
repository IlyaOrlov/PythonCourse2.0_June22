import numpy as np

def fun(arr):
    a = 5
    s = len(arr)
    c = 0
    new = []
    while c < s - 1:
        for i in arr:
            for j in i:
                if j == a:
                    new.append(i)
        c += 1
    np.delete(arr, new, 0)
    print(arr)

arr = [[1, 5, 8], [7, 2, 9], [4, 3, 1]]
fun(arr)
