N = int(input())
string = ''
if N % 4 !=0 and (N + 1) % 4 !=0:
	print('IMPOSSIBLE')
else:
	min_possable = (-1 - N) * (N / 2)
	for num in range(N, 0, -1):
		if min_possable + 2*num <= 0:
			min_possable += 2*num
			string = '+'  + string
		else:
			string = '-' + string
	print(string)