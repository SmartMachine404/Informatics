A = int(input())
B = int(input())
C = int(input())
a = min(A, B)
b = min(A, C)
c = min(B, C)
if a==b:
	print(min(B, C))
elif b==c:
	print(min(A, B))
else:
	print(min(A, C))