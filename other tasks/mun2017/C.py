hu1, mu1, su1 = [int(x) for x in input().split(':')]
hs, ms, ss = [int(x) for x in input().split(':')]
hu2, mu2, su2 = [int(x) for x in input().split(':')]

tu1 = hu1 * 3600 + mu1 * 60 + su1

ts = hs * 3600 + ms * 60 + ss
if ts < tu1:
	ts += 86400

tu2 = hu2 * 3600 + mu2 * 60 + su2
if tu2 < tu1:
	tu2 += 86400

delay = (tu2 - tu1 + 1) // 2
real_time = ts + delay

r_hours = real_time // 3600
r_min = real_time % 3600 // 60
r_sec = real_time % 3600 % 60

r_hours %= 24
if r_hours < 10:
	r_hours = '0' + str(r_hours)
if r_min < 10:
	r_min = '0' + str(r_min)
if r_sec < 10:
	r_sec = '0' + str(r_sec)

print(f"{r_hours}:{r_min}:{r_sec}")