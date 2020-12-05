n = int(input())
if n >= 1000:
	s_max = n // 100
	s_min = n % 100
else:
	s_max = n //10
	s_min = n %10

n1 = min(9, s_min)
n2 = s_min - n1
n3 = min(9, s_max)
n4 = s_max - n3
if n2 == 0 :
	n2 = 1
	n1 -=1
if s_max > 18 or s_min > 18:
	print(0)
elif s_min == 0:
	print(n4, n3, 0, 0, sep='')	
else:
	print(n2, n1, n4, n3, sep='')