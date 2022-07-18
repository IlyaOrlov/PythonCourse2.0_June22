def fun(arr):
	a = 20
	count = 0
	for i in arr:
		for j in i:
			if j == a:
				del(arr[count])
				count += 1
	print(arr)

arr1 = [20, 22, 17]
arr2 = [18, 21, 18]
arr3 = [21, 20, 19]

arr = ([arr1, arr2, arr3])
fun(arr)