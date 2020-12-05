#!/usr/bin/python3
start = int(input())
stop = int(input())
rotation = int(input())
d_t = stop - start
ans = 0
i = rotation
while d_t >= i:
	ans += d_t - i + 1
	i += rotation
print(ans)
