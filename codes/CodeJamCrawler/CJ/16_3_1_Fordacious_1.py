def translatemoves (moves):
	string = ""
	if moves == None:
		return "ERROR"
	for i in moves:
		for j in i:
			string += chr(ord("A") + j)
		string += " " 
	return string

def ismaj_remove2 (parties, i, j, total):
	if total <= 0:
		return False
	parties[i] -= 1
	parties[j] -= 1
	for k in parties:
		if k / total > 0.5:
			parties[i] += 1
			parties[j] += 1
			return True
	parties[i] += 1
	parties[j] += 1
	return False

def ismaj_remove1 (parties, i, total):
	if total <= 0:
		return False
	parties[i] -= 1
	for j in parties:
		if j / total > 0.5:
			parties[i] += 1
			return True
	parties[i] += 1
	return False

def copy(parties):
	return parties[:]

def dfs (parties):
	total = 0
	for i in parties:
		total += i
	if total == 0:
		return []
	for i in range(len(parties)):
		if parties[i] > 0 and ismaj_remove1(parties, i, total - 1) == False:
			p = copy(parties)
			p[i] -= 1
			rest = dfs(p)
			if rest != None:
				return [[i]] + (rest)
		for j in range(len(parties)):
			if i != j and parties[i] > 0 and parties[j] > 0 and ismaj_remove2(parties, i, j, total - 2) == False:
				p = copy(parties)
				p[i] -= 1
				p[j] -= 1
				rest = dfs(p)
				if rest != None:
					return [[i,j]] + (rest)
	return None

def getint():
	return int(input())

t = getint()
for i in range(t):
	n = getint()
	parties = []
	partiesStr = input().split(" ")
	for k in partiesStr:
		parties.append(int(k))
	print("Case #" + str((i+1)) + ": " + str(translatemoves(dfs(parties))))