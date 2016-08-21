from collections import deque

adj = {}
seen = {}
distance = {}
INFINITY = -1

def initialize():    
    adj.clear()
    seen.clear()
    distance.clear()


def flip(s):
	r = s[::-1]

	f = ''
	for c in r:
		if c == '+':
			f += '-'
		else:
			f += '+'
	#print("reversed:{} flipped:{}".format(r, f))
	return f

def generateAdj(s):
	lens = len(s)
	adjs = []
	for i in range(1,lens+1):
		a = flip(s[:i])
		b = s[i:]
		#print('a:{} b:{}'.format(a,b))
		adjs.append(a+b)
		if (a+b) not in seen:
			seen[a+b] = False
	return adjs


def solve(s, t):
    seen[s] = True
    distance[s] = 0
    queue = deque([s])
    while len(queue) > 0:
        u = queue.popleft()
        #print("analizing: {}".format(u))
        if u == t:
        	return distance[u]
        adj[u] = generateAdj(u)
        #print("adj: {}".format(adj[u]))
        for v in adj[u]:
            if not seen[v]:
                seen[v] = True
                distance[v] = distance[u] + 1
                queue.append(v)

	
t = int(input().strip())
for x in range(t):
	s = input().strip()
	initialize()
	print("Case #{0}: {1}".format(x+1, solve(s, '+'*len(s))))
