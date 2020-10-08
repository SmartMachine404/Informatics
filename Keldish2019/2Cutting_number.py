l = int(input())
n = int(input())
power = l//2
while True:
	left = n // 10**power
	right =  n % 10**power
	if right < 10**(power - 1):
		power += 1
	else:
		break
pair1 = (left, right)

power = l//2
while True:
	left = n // 10**power
	right =  n % 10**power
	if right < 10**(power - 1):
		power -= 1
	else:
		break
pair2 = (left, right)

print(min(  pair1[0]+pair1[1] ,  pair2[0]+pair2[1] ))