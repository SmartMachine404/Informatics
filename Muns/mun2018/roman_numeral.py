numerals = {
	'I': 1,
	'V': 5,
	'X': 10,
	'L': 50,
	'C': 100,
	'D': 500,
	'M': 1000,
	'IV': 4,
	'IX': 9,
	'XL': 40,
	'XC': 90,
	'CD': 400,
	'CM': 900
}

s = input()
i = len(s) - 1
a = 0
while i >= 0:
	num1 = s[i]
	num2 = s[i-1:i+1]
	if i > 0 and num2 in numerals:
		a += numerals[num2]
		i -= 2
	else:
		a += numerals[num1]
		i -= 1
print(a)