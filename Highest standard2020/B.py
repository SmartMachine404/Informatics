t = int(input())
b = [int(x) for x in input().split()]
e = int(input())
i = 0
for tree in range(e):
	l, r = [int(x)-1 for x in input().split()]
	steps = (r - l + 1) // 2
	for city in range(0, steps):
		n = city + 1
		num_toys = (n+1)*n/2
		city_b = b[l + city]*num_toys
		i += city_b
	for city in range(steps, 2*steps):
		n = 2*steps - city
		num_toys = (n+1)*n/2
		city_b = b[l + city]*num_toys
		i += city_b
	print(int(i)%998244353)
	i=0