capacity = int(input())
N = int(input())
time = 0
people = [0]*N
for f in range(N):
	p = int(input())
	people[f] = p%capacity
	time += 2*(p//capacity)*(f+1)

full = 0
empty= 1

f = N-1
while f >= 0:
	if people[f] != 0:
		if empty:
			time += 2*(f+1)
			empty = 0
		free = capacity-full
		full += min(people[f], free)
		people[f] -= min(people[f], free)
		if full == capacity:
			full = 0
			empty = 1
			f+=1
	f-=1
print(time)
