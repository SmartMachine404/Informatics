n = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a*d > c*b:
	m = n//a * b
	r = n%a
	m += min(b, r, r//c*d + r%c, (r + c - 1)//c*d)
else:
	m = n//c * d
	r = n%c
	m += min(d, r, r//a*b + r%a, (r + a - 1)//a*b)

print(m)