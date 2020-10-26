#Done!
t = int(input())
n = int(input())
ab = [(int(input())+t*(i%2==1), 0 if i%2==0 else 1) for i in range(2*n)]
m = int(input())
cd = [(int(input())+t*(i%2==1), 2 if i%2==0 else 3) for i in range(2*m)]

table = sorted(ab + cd)
trains = 0
available = [0, 0, 0, 0]
for s in range(0, len(table) - 1):
	i1 = table[s][1]

	if available[i1] > 0:
		available[i1] -= 1
		available[(i1 + 1)%4]+=1
		continue

	if s < len(table) - 1 and table[s][0] == table[s+1][0] and available[table[s + 1][1]] > 0:
		table[s], table[s + 1] = table[s + 1], table[s]
		i1 = table[s][1]
		available[i1] -= 1
		available[(i1 + 1)%4]+=1
		continue

	if s < len(table) - 2 and table[s][0] == table[s+2][0] and available[table[s + 2][1]] > 0:
		table[s], table[s + 2] = table[s + 2], table[s]
		i1 = table[s][1]
		available[i1] -= 1
		available[(i1 + 1)%4]+=1
		continue

	trains += 1
	available[(i1 + 1)%4]+=1

print(trains)
