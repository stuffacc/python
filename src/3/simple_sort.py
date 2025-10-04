arr = [0, 15, 105, 1, -2, 304, 4, 34, 6, 7, 39, 53]

def simple_sort(arr):
	for i in range(len(arr)):
		for j in range(1, len(arr)):
			if arr[j-1] > arr[j]:
				arr[j-1], arr[j] = arr[j], arr[j-1]

	return arr


print(arr)
print(simple_sort(arr))