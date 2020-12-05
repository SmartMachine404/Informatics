lines = int(input())
columns = int(input())
house = [input() for i in range(lines)]
lake = [input() for i in range(lines)]
ans = 0
for dy in range(-lines, lines + 1):	
	for dx in range(-columns, columns + 1):
		count = 0
		for y in range(lines):
			for x in range(columns):
				if house[y][x] == 'H':
					x_water, y_water = x + dx, y + dy
					if 0 <= x_water < columns and 0 <= y_water < lines and lake[y_water][x_water] == 'W':
						count = -10 ** 9
					for xx, yy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
						x_water = dx + x + xx
						y_water = dy + y + yy
						if 0 <= x_water < columns and 0 <= y_water < lines and lake[y_water][x_water] == 'W':
							count +=1
		ans = max(ans, count)
print(ans)
