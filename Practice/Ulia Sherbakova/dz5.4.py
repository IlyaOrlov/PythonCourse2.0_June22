def fun(arr, a):
    s = len(arr)
    count2 = 0
    while count2 < len(arr[count2]):
        found = False
        for row in arr:
            if row[count2] == a:
                found = True
                break
        if found:
            count1 = 0
            while count1 < s:
                del (arr[count1][count2])
                count1 += 1
        else:
            count2 += 1
    print(arr)

arr = [[20, 20, 20], [18, 21, 18],[21, 20, 19]]
a = 20
fun(arr, a)