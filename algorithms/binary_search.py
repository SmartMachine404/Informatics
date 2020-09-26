def binary_search_in_range(minimum, maximum):
	more = True
	less = False
	left = minimum
	right = maximum
	while right - left > 1:
		middle = (right + left)//2 - 1
		answer = int(input(f'Is your number more than {middle}? [{left} {right}) '))
		if answer == more:
			left = middle + 1
		else:
			right = middle + 1
	print(f'Your number is {left}')


def bin_search(arr, item):
	""" if item in arr that return index, else return -1"""
	left = -1
	right = len(arr)
	while right - left > 1:
		middle = (right + left) // 2
		if arr[middle] > item:
			right = middle
		elif arr[middle] < item:
			left = middle
		else:
			return middle
	return -1

def first_entry(arr, item):
	"""return index of first entry or -1"""
	left = 0
	right = len(arr) 
	while right - left > 1:
		middle  = (right + left) // 2
		if arr[middle] >= item:
			right = middle
		else:
			left = middle + 1
	if arr[right] == item:
		return right
	else:
		return -1