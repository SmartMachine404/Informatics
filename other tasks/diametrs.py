t = int(input())
n = int(input())
ab = [(int(input())+t*(i%2==1), 0 if i%2==0 else 1) for i in range(2*n)]
m = int(input())
cd = [(int(input())+t*(i%2==1), 2 if i%2==0 else 3) for i in range(2*m)]

table = sorted(ab + cd)
trains = 1
available = [0, 0, 0, 0]
for s in range(0, len(table) - 1):
	i1 = table[s][1]
	available[(i1 + 1)%4]+=1
	i2 = table[s + 1][1]
	# if table[s][0] == table[s + 1][0]:
	# 	print('eq')
	# 	if (i2+1)%4 == i1:
	# 		table[s], table[s + 1] = table[s + 1], table[s]
	# 		print('changed')
	# 		continue
	if available[i2] > 0:
		available[i1] = max(available[i1]-1, 0)

	elif available[i2] <= 0:
		if s < len(table) - 2 and table[s+1][0] == table[s+2][0] and available[table[s + 2][1]]:
			table[s + 1], table[s + 2] = table[s + 2], table[s + 1]
			available[i1] = max(available[i1]-1, 0)
		else:
			trains +=1
			available[(i2 + 1)%4]+= 1
print(trains)
# stack = []
# if departure_a.pop(0) <= departure_b.pop(0):
# 	stack.append
# else:
# 	position_is_a = False
# for x in range(min(n, m)):
# 	if arrival_a[x] > departure_a[x] or arrival_b[x] > departure_b[x]:
# 		trains+=1
# print(trains)