# COMPLETED!
a = int(input())
b = int(input())
n = int(input())
m = int(input())
min_a = n * (a + 1) - a
max_a = n * (a + 1) + a
min_b = m * (b + 1) - b
max_b = m * (b + 1) + b

if min_a > min_b:
	glob_min = min_a
else:
	glob_min = min_b

if max_a < max_b:
	glob_max = max_a
else:
	glob_max = max_b

if glob_min > glob_max:
	print(-1)
else:
	print(glob_min, glob_max)