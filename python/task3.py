from collections import defaultdict

def color_graph(defaultdict graph):
	pass

line = raw_input()
values = map(int, line.split())
N = values[0]
M = values[1]

graph = defaultdict()
for i in range(N):
	graph[i] = ''

edge = {}

# read graph
for i in range(M):
	line = raw_input()
	values = map(int, line.split())
	graph[values[0]] = graph[values[1]]
	graph[values[1]] = graph[values[0]]
	edge[i] = values

# read Q
line = raw_input()
values = map(int, line.split())
Q = values[0]

# read cuts
line = raw_input()
values = map(int, line.split())

for x in range(Q):
	graph[edge[values[x]]]