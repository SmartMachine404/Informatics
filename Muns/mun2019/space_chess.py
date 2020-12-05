xe = int(input())
ye = int(input())
sign_x = -1 if xe < 0 else 1
sign_y = -1 if ye < 0 else 1
x, y = 0, 0

if abs(xe) > abs(ye):
	kff_xe = 2
	kff_ye = 1
else:
	kff_xe = 1
	kff_ye = 2

while min(abs(x), abs(y)) < min(abs(xe), abs(ye)):
	x += sign_x * kff_xe
	y += sign_y * kff_ye
	print(x, y)
if x == xe and y == ye:
	exit()

if x == xe:
	move_x = False
	sign = (ye - y) // abs(ye - y)

elif y == ye:
	move_x = True
	sign = (xe - x) // abs(xe - x)


while x != xe or y != ye:
	if move_x:		
		x +=  2 * sign
		y -= 1
		print(x, y)
		x += 2 * -sign
		y -= 1
		print(x, y)
		x += sign
		y += 2
		print(x, y)
	else:
		y +=  2 * sign
		x -= 1
		print(x, y)
		y += 2 * -sign
		x -= 1
		print(x, y)
		y += sign
		x += 2
		print(x, y)
