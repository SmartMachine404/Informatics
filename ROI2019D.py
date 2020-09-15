n = int(input())
RIGHT = n + 1
LIED = False
status  = 'Correct'

while status != 'Done':
	#Scaning planet:
	left = 1
	right = RIGHT
	lied = False
	while right - left > 1:
		middle = (left + right)//2
		ask = f'? {middle}'
		answer = input(ask)
		if not lied:
			answer2 = input(ask)
			if answer != answer2:#if lied
				lied = True
				answer = input(ask)

		if answer == 'Yes':
			left = middle
		else:
			right = middle
	status = input(f'! {left}')

		