line = raw_input()
N = map(int, line.split())[0]

line = raw_input()
values = map(int, line.split())

result = 0

for i in range(1, N + 1):
	arr = sorted(values[:i], reverse=True)
	result = result + arr[i/2]

print "{}".format(result)