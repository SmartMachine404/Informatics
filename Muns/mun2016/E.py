n = int(input())
price = int(input())
print(price)
olds = [price + price//3]
oldptr = 0
for i in range(n-1):
	price = int(input())
	if oldptr != len(olds) and price == olds[oldptr]:
		oldptr+=1
	else:
		print(price)
		olds.append(price+price//3)