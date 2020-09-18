def binary_search(element, arr):
	left = 0
	right = len(arr)
	while right - left > 1:
		middle = (right + left) // 2
		if element > arr[middle]:
			left = middle + 1
		elif element < arr[middle]:
			right = middle
		else:
			return middle
	return left
