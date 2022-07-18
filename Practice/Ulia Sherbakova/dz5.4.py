def fun(arr):
    a = 20
    s = len(arr)
    count1 = 0
    count2 = 0
    while count1 < s and count2 < s:
        for i in arr:
            for j in i:
                if j == a:
                    del(arr[count1][count2])
                    count1 += 1
                    count2 += 1
    print(arr)

arr = [[20, 20, 20],
       [18, 21, 18],
       [21, 20, 19]]
fun(arr)