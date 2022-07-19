import numpy as np

def fun(arr):
    a = 5
    s = len(arr)
    c = 0
    while c < s - 1:
        for i in arr:
            for j in i:
                if j == a:
                    np.delete(arr, c, 0)
        c += 1
    print(arr)

arr = [[1, 5, 8], [7, 2, 9], [4, 3, 1]]
fun(arr)
