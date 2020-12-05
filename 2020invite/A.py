a = int(input())
n = int(input())

b = n + a
if a < 0 and b >=0:
	b +=1
if  a > 0 and b <=0:
	b-=1
print(b)