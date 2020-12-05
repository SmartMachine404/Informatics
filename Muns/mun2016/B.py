from math import gcd
# def gcd(x, y):
# 	while y != 0:
# 		x, y = y, x%y
# 	return x
a = int(input())
b = int(input())
c = int(input())
d = int(input())
operations = 0
while a*d < c*b:
	a += 1 
	b += 1
	g = gcd(a,b)
	a //= g
	b //= g
	operations += 1
if a == c and b == d:
	print(operations)
else:
	print(0)
