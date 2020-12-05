v = int(input())
s = v//(16*3)
v %= 16*3
a = v//16
v %= 16
p = v // 4
v %= 4
print(s, a, p, v)