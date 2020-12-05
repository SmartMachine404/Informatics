N = int(input())
old_list = list(range(1, N+1))

i=0
new_list = []
while len(old_list) > 1:
	winner = int(input()) -1
	new_list.append(old_list[2*i + winner])
	i+=1
	if 2 * len(new_list) == len(old_list):
		i = 0
		old_list = new_list
		new_list = []
print(old_list[0])