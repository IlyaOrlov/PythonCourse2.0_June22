def sort(arr):
    n = len(arr)
    i = 0
    while i < n - 1:
        m = i
        j = i + 1
        while j < n:
            if arr[j] < arr[m]:
                m = j
            j += 1
        arr[i], arr[m] = arr[m], arr[i]
        i += 1

    print(arr)


sort([0,3,24,2,3,7])