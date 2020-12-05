def sign(x):
	if  x >= 0:
		return 1
	else:
		return -1

x_finish = int(input())
y_finish = int(input())
x, y = 0, 0

while abs(x_finish - x) > 0 and abs(y_finish - y) > 0:
	if abs(x_finish - x) >= abs(y_finish - y):
		x += sign(x_finish - x) * 2
		y += sign(y_finish - y)
	else:
		x += sign(x_finish - x) 
		y += sign(y_finish - y) * 2
	print(x, y)
while x_finish - x != 0 or y_finish - y != 0:
	if abs(y_finish - y) > 0:
		x += 2
		y += sign(y_finish - y)
		print(x, y)
		x -= 1
		y += sign(y_finish - y) *2
		print(x, y)
		x -= 1
		y +=  sign(y_finish - y) *2
		print(x, y)

	elif abs(x_finish - x) > 0:
		y += 2
		x += sign(x_finish - x)
		print(x, y)
		y -= 1
		x += sign(x_finish - x) *2
		print(x, y)
		y -= 1
		x +=  sign(x_finish - x) *2
		print(x, y)