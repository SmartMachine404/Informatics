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
binary_search_in_range(1, 120)