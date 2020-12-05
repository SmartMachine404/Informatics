n = int(input())
a = [int(input()) for i in range(n)]
a.sort(reverse=True)
k = [0] * n
for x in range(n):
	k[x] = (x + 1) * a[x]
u = k.index(max(k))
print(u + 1, a[u])