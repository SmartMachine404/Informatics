a = int(input())
b = int(input())


if (a + b) % 3 != 0:
	print(-1)
elif a > b*2 or b > 2*a:
	print(-1)
else :
	ba = a // 2
	bb = b // 2 
	sa = a % 2
	sb = b % 2
	if ba % bb ==0 and sa % sb ==0:
		pritn(ba, bb)
	else :
		print(-1)