n = int(input())
min_sqrt = int(n**0.5)

if n - min_sqrt**2 <= min_sqrt + 1:
	x = min_sqrt**2 + 1
	y = n - k**2
else:
	x = (min_sqrt + 1)**2 - n + 1
	y = (min_sqrt + 1)**2

if (min_sqrt+1)%2==0:
	print(x, y)
else:
	print(y, x)
