ticket = input()
n = len(ticket)

if ticket == '9'*n:
	print(('0'*(n//2-1)+'1')*2)

else:
	ticket = list(map(int, ticket))
	sum1 = sum(ticket[0:n//2])
	sum2 = sum(ticket[n//2::])

	d = n-1
	while sum2 >= sum1:
		sum2 -= ticket[d]
		ticket[d]=0
		ticket[d-1] += 1
		if d-1 > n//2:
			sum2 += 1
		else:
			sum1 += 1

		i = d-1
		while ticket[i] > 9:
			
			if i-1 > n//2:
				sum2 += 1
			else:
				sum1 += 1
			ticket[i-1]+=1

			if i > n//2:
				sum2 -= ticket[i]
			else:
				sum1 -= ticket[i]
			ticket[i]=0
			i-=1

		d-=1

	if sum2 < sum1:
		for d in range(n-1, n//2-1, -1):
			tmp = min(9 - ticket[d], sum1 - sum2)
			ticket[d] += tmp
			sum2 += tmp
	
	for i in ticket:
		print(str(i), end='')
	print()