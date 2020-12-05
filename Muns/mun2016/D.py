n = int(input())
p = int(input())
k = int(input())

if p % 2 == 0:
	p_pos = (p - k) % n

	n1_pos = (p_pos + 1) % n
	n1 = (n1_pos - k) % n
	
	n2_pos = (p_pos - 1) % n
	n2 = (n2_pos - k) % n
else:
	p_pos = (p + k) % n

	n1_pos = (p_pos + 1) % n
	n1 = (n1_pos + k) % n
	
	n2_pos = (p_pos - 1) % n
	n2 = (n2_pos + k) % n

if n1 == 0:
	n1 = n
elif n2 == 0:
	n2 = n
print(min(n1, n2), max(n1, n2))