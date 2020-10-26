numerals = {
	'I': 1,
	'V': 5,
	'X': 10,
	'L': 50,
	'C': 100,
	'D': 500,
	'M': 1000
}
nums_string = input()
new_string = ''

for l in range(len(nums_string)-1):
	
	letter = nums_string[l]
	value = numerals[letter]

	next_letter = nums_string[l + 1]
	next_value = numerals[next_letter]

	new_string += letter

	if 2 * value >= next_value or (10 * value < next_value and next_letter in ['L', 'D']):
		new_string += ' '
new_string += nums_string[-1]

summ = 0
splited = new_string.split(' ')
for i in splited:
	if len(i)==1:
		summ += numerals[i]
	else:
		u = 0
		for c in range(len(i)-1, -1, -1):
			letter = i[c]
			if u % 2 == 0:
				summ += numerals[letter]
				
			else:
				summ -= numerals[letter]
			u += 1

print(splited)
print(summ)
