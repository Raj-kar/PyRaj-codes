# Sorting - Algo -> bubble sort, Quick sort

# [11, 2, 311, 43] = [2, 11, 43, 311]

def bubblesort(arr):
	n = len(arr)

	for i in range(n):
		for j in range(0, n-i-1):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]

	for i in range(n):
 		print(arr[i], end = ' ')


arr = [4, 6, 11, 5, 1, 66, 87, 31]
# [4, 6, 5, 11, 1, 66, 87, 31]
# [4, 6, 5, 1, 11, 66, 87, 31]
# [4, 6, 5, 1, 11, 66, 31, 87]

# [4, 5, 6, 1, 11, 66, 31, 87]
# [4, 5, 1, 6, 11, 66, 31, 87]
# [4, 5, 1, 6, 11, 31, 66, 87]

bubblesort(arr)