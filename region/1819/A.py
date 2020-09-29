l = int(input())
r = int(input())
a = int(input())
d_t = r - l
d_i = range(a, d_t + 1, a)

summ = 0
for i in d_i:
	summ += (d_t - i + 1)
print(summ)