n = int(input())
sizes = [int(input()) for i in range(n)]

def check(player):
	if sizes[player] == sizes[0]:
		return 0
	s = sum(sizes[0:player+1])
	for g in sizes[player+1::]:
		if g < s:
			s += g
		else:
			return 0
	return 1

if len(sizes) == 1:
	p = 0
elif sizes[-1] == sizes[0]:
	p = n
else:
	last_loser = 0
	first_winner = n-1
	while first_winner - last_loser > 1:
		mid = (first_winner + last_loser)//2
		if check(mid):
			first_winner = mid
		else:
			last_loser = mid
	p = first_winner

for i in range(n):
	if i >= p:
		print(1)
	else:
		print(0)