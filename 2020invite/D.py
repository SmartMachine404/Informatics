n = int(input())
start_ans = 0
finish_ans = 0
prev_height = 10**9
last_height = 10**9
last_len = 0
min_len = 10**9

for i in range(1, n + 1):
	h = int(input())
	
	if h == last_height:
		last_len +=1
	
	else:
		if prev_height < last_height > h and last_len < min_len:
			min_len = last_len
			start_ans = i - last_len - 1
			finish_ans = i
		prev_height = last_height
		last_height = h
		last_len = 1

if start_ans == 0:
	print(0)
else:
	print(start_ans)
	print(finish_ans)