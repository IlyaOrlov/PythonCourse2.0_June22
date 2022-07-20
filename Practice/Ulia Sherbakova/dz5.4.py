def fun(arr, a):
    s = len(arr)
    count2 = 0
    new = []
    while count2 < len(arr[count2]):
        new.clear()
        for row in arr:
            new.append(row[count2])
        if a in new:
            count1 = 0
            while count1 < s:
                del(arr[count1][count2])
                count1 += 1
        else:
            count2 += 1
    print(arr)

arr = [[20, 20, 20], [18, 21, 18],[21, 20, 19]]
a = 20
fun(arr, a)