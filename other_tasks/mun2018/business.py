#!/usr/bin/python3

floors = workers = int(input())
up = int(input())
down = int(input())
lift = int(input())

for f in range(1, floors + 1):
	
	for worker in range(1 , workers + 1):
		delta = worker - f

		if delta >= 0:
			by_lift = delta * up + f * lift
		else:
			by_lift = -delta * down + f * lift

		by_ladder = worker * up

		optimal = min(by_lift, by_ladder)
		
		if worker == 1:
			max_on_floor = optimal

		if optimal > max_on_floor:
			max_on_floor = optimal
	
	if f == 1:
		optimal_time = max_on_floor

	if max_on_floor < optimal_time:
		optimal_time = max_on_floor 

print(optimal_time)
