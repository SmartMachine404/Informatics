x, y, z = [int(x) for x in input().split()]
rest_y = y % z
rest_x = x % z
need_x = z - rest_x
need_y = z - rest_y
can_move_yx = rest_y >=need_x
can_move_xy = rest_x >=need_y
if can_move_xy and can_move_yx:
	can_buy = x // z + y // z + 1
	move = min(need_y, need_x)
	print(can_buy, move)
elif can_move_yx:
	can_buy = x // z + y // z + 1
	print(can_buy, need_x)
elif can_move_xy:
	can_buy = x // z + y // z + 1
	print(can_buy, need_y)
else:
	can_buy = x // z + y // z
	print(can_buy, 0)