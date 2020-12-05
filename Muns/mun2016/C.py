a = input()
b = input()
c = 0
bgens = {b[i:i+2] for i in range(len(b) - 1)}
for i in range(len(a)-1):
	if a[i:i+2] in bgens:
		c+=1
print(c)