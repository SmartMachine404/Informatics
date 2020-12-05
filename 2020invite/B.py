a = int(input())
b = int(input())
c = int(input())
cycles = min(a, b//2, c)
a -= cycles
b -= 2*cycles
c -= cycles
t = 4* cycles
if a != 0:
	t+=1
	if b!= 0:
		t +=1
		if c != 0:
			t+=1
print(t)