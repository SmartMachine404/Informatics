A = int(input())
B = int(input())
if A % 2 != B % 2:
	if A % 2 == 1:
		A +=1
	else:
		B += 1
if A > B:
	distance = A - B
else:
	distance = B - A
print((distance)//2)