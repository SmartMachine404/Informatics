m = int(input())
a = 1
max_part = 0
while a**2 <= m:
	if m % a**2 == 0:
		max_part = a**2
	a += 1
print(max_part)
