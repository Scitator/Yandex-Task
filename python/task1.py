line = raw_input()
N = map(int, line.split())[0]

line = raw_input()
values = map(int, line.split())

sum_M = 0.0
for x in values:
	sum_M += float(x) / 2.0

if N == 1:
	print "{}/{}".format(int(sum_M), 1)
else:
	N2 = (N ** 2 - 1)
	a = sum_M % N2
	for x in reversed(range(int(sqrt(a)))):
		if a % x == 0 and N2 % x == 0:
			a = a/x