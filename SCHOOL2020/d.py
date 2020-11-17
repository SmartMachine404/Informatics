n = int(input())
sizes = [int(input()) for i in range(n)]
p = [0] * n
p[-1] = 1

summ = sum(sizes)
up = sizes[-1]

for gamer in range(n-2, -1, -1):
	if summ - up > sizes[gamer+1]:
		p[gamer] = 1
		up += sizes[gamer]
	else:
		break

if p[-1] == p[0]:
	p = [0]*n

for i in p:
	print(i)