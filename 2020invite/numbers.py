ca = a = int(input())
s_a = 0
cb = b = int(input())
s_b = 0
p = 1

while ca > 0:
	s_a += ca % 10
	ca //= 10

while cb > 0:
	s_b += cb % 10
	cb //= 10


odd_a = a//10 * 5 + (a%10 + 1)//2
odd_b = b//10 * 5 + (b%10 + 1)//2
print(odd_b - odd_a + ca % 2)