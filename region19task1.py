n, m = [int(x) for x in input().split()]
x1, y1, x2, y2 = [int(x) for x in input().split()]
dx = x2 - x1
dy = y2 - y1
gx, gy = 0, 0
if dx != 0 and dy != 0:
	if dx > 1:
		gx = x2 - 1
		gy = y1
	elif dx < -1:
		gx = x2 + 1
		gy = y1
	elif dy > 1:
		gy = y2 - 1
		gx = x1
	elif dy < -1:
		gy = y2 + 1
		gx = x1

print(gx ,gy)