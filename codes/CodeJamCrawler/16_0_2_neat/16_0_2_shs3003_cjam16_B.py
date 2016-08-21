
cost = dict()
vis = set()
goal = ""

def flip(S, pos):
	new_s = ""
	for i in xrange(pos-1,-1,-1):
		if S[i]=='+':
			new_ch = '-'
		else:
			new_ch = '+'
		new_s += new_ch
	
	for i in xrange(pos,len(S)):
		new_s += S[i]
	
	return new_s

def find_cost(S):
	global cost, goal
	cost[S] = 0
	queue_s = [S]
	prev_map = dict()
	prev_map[S] = None
	visited = set()
	visited.add(S)
	while len(queue_s)>0:
		cur_s = queue_s[0]
		prev_s = prev_map[cur_s]
		
		if cur_s not in cost.keys():
			cost[cur_s] = 1000000000
		
		if prev_s!=None:
			cost[cur_s] = min(cost[cur_s], cost[prev_s]+1)
		
		#print cur_s, prev_s, cost[cur_s]
		
		if cur_s==goal:
			break
		
		del queue_s[0]
		#new_s_ls = []
		for pos in range(1,len(cur_s)+1):
			new_s = flip(cur_s, pos)
			if new_s not in visited:
				visited.add(new_s)
				prev_map[new_s] = cur_s
				#new_s_ls.append(new_s)
				queue_s.append(new_s)
	
		
	cur_s = goal
	# print 'Path:'
	# while cur_s!=None:
		# print cur_s
		# cur_s = prev_map[cur_s]
	
	
def solve(S):
	global goal
	goal = ""
	for i in xrange(len(S)):
		goal += '+'
	
	#print "S:",S
	find_cost(S)
	return cost[goal]
	
if __name__ == "__main__":
	T = int(raw_input())
	
	for t in range(T):
		S = raw_input()
		cst = solve(S)
		#print cost
		print "Case #{0}: {1}".format(t+1,cst)
		cost.clear()