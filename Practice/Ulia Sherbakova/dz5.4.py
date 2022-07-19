def fun(arr):
    a = 20
    s = len(arr)
    count1 = 0
    count2 = 0
    while count1 < s - 1 and count2 < s - 1:
        for i in arr:
            for j in i:
                if j == a:
                    del(arr[count1][count2])
                    count2 += 1
            else:
                count1 += 1
    print(arr)

arr = [
       [1, 20, 20],
       [18, 21, 18],
       [21, 20, 19]
]
fun(arr)
