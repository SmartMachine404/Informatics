l = int(input())
n = int(input())
ptr = 0
ans = 0
for b in range(n):
	s = int(input())
	if s == 1 and b >= ptr:
		ans +=1
		ptr = b + l
print(ans)