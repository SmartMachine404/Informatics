a = int(input())
b = int(input())
n = 0
def sn(x):
	c = x
	s = 0
	while c > 0:
		s += c%10
		c //= 10
	return s % 2

while a <= b and a%10 != 0:
	n+=sn(a)
	a +=1

if a < b:
	n += (b - a) // 10 * 5
	a += (b - a) // 10 * 10

while a <= b:
	n+=sn(a)
	a+=1
print(n)