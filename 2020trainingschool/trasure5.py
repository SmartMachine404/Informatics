way = input()
way_with_spaces = way
up = 0
right = 0
for liter in ['N', 'E', 'S', 'W']:
	way_with_spaces = way_with_spaces.replace(liter, liter + ' ')
arr = way_with_spaces.split(' ')
for step in arr[:-1]:
	if step[-1]=='N':
		up += int(step[:-1])
	elif step[-1]=='S':
		up -= int(step[:-1])
	elif step[-1]=='E':
		right += int(step[:-1])
	elif step[-1]=='W':
		right -= int(step[:-1])

if up > 0:
	up_l = 'N'
elif up < 0:
	up_l = 'S'
	up = -up

if right > 0:
	right_l = 'E'
elif right < 0:
	right_l = 'W'
	right = -right

if up != 0:
	up_c = str(up) + up_l
else:
	up_c = ''

if right != 0:
	right_c = str(right) + right_l
else:
	right_c = ''

compose = up_c + right_c
print(compose)