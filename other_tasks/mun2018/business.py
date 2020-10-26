#!/usr/bin/python3

floors = workers = int(input())
up = int(input())
down = int(input())
lift = int(input())
statistics = [f * up for f in range(1, workers + 1)]
for f in range(1, floors + 1):
	for worker in range(1 , workers + 1):
		delta = worker - f
		if delta >= 0:
			time = delta * up + f * lift
		else:
			time = -delta * down + f * lift
		
		if time <= statistics[worker - 1]:
			statistics[worker - 1] = time
print(max(statistics))
