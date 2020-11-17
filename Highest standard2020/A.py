n = int(input())
c = [0]*10
x=1
d=1
while n > 0:
	n //=10
	for i in range(1, 10):
		c[i] += n*x 
	c[0] = int(c[0]+0.1*x*n)
	x*=10
	# for i in range(0, n%10+1):
	# 	c[i]+=1
for i in c:
	print(i)