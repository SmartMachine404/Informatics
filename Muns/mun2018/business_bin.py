n = workers = int(input())
up = int(input())
down = int(input())
lift = int(input())

def time(x, y):
	return max(up * y, lift * x + (x - y - 1) * down, lift * x + (n - x) * up)

x1 = (n*up*down + n*up*up) // (up*up + 2*up*down - lift*down)
x2 = x1 + 1
y1 = x1*(lift + down) // (up + down)
y2 = x2*(lift + down) // (up + down)

print(min(time(x1, y1), time(x2, y2)))
