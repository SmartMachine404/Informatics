"""
Task: https://old.informatics.msk.ru/mod/statements/view.php?id=41903#1
"""
str_m_n = input().split()
str_seq = input().split()

num_markers = int(str_m_n[0])
num_colors = int(str_m_n[1])
sequence = [int(color) for color in str_seq]
k=0
opened_colors = []
locked_colors = []
line = []
A = []
B = []
iteration = 0
for cur in sequence:
	if cur in locked_colors:
		print(-1)
		exit()
	if cur in opened_colors:
		cur_index = opened_colors.index(cur)
		locked_colors += opened_colors[cur_index+1:]
		opened_colors = opened_colors[:cur_index+1]
		B[line.index(cur)] = iteration
	else:
		opened_colors.append(cur)
		line.append(cur)
		A.append(iteration)
		B.append(iteration)
		k+=1
	iteration += 1

print(k)
for c, a, b  in zip(line, A, B):
	print(f'{c} {a+1} {b+1}') 
