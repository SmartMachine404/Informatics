N = int(input())
M = int(input())
K = int(input())
for i in range(K):
	press = int(input())
	selected_window = press % N + 1
	if selected_window == M:
		M = 1
	elif selected_window > M:
		M += 1
print(M)