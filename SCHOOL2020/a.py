k = int(input())
n = int(input())

d1 = n % k
d2 = k - d1
print(min(d1, d2))