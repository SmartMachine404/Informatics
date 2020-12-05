n = int(input())
X = [0] * n
Y = [y for y in range(1, n+1)]

for x in range(n):
	X[x] = int(input())

Xnew =[0]*n
Ynew = Xnew
for l in range(n):
	Xnew[X[l]-1] = n+1 -Y[l]
for i in range(n):
	print(Ynew[i])