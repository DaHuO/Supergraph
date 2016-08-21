import sys
sys.setrecursionlimit(10000)

def solving(string):
	PARTY = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	parties = string.split()
	parties = [int(n) for n in parties]
	l = len(parties)
	total = sum(parties)
	eva = 0
	eva_list = []
	rest = total
	# print total
	while eva != total:
		e = []
		majority = (rest - 2) / 2 + 1
		# print parties, majority
		for i,n in enumerate(parties):
			if len(e) == 2 or rest - len(e) == 2:
				break
			if n == majority + 1:
				e += [i,i]
			elif n == majority:
				e += [i]
			elif n > majority+1:
				print 'error'
		B = 2
		if rest == 3:
			B = 1
		if len(e) == 0:
			for i,n in enumerate(parties):
				if len(e) == B:
					break
				if n > 0:
					if n > 1:
						e += [i]
					elif i not in e:
						e += [i]

		eva += len(e)
		eva_list.append(e)
		rest = total - eva
		if rest < 0:
			print 'error', parties, e
			break
		for j in e:
			parties[j]-=1
	eva_list_alpha = [ ''.join([PARTY[n] for n in e]) for e in eva_list]

	return ' '.join(eva_list_alpha)

with open('input', 'r') as input:
	count = 0
	for line in input:
		if count == 0:
			count+=1
			continue
		if count % 2 == 1:
			count+=1
			continue
		print 'Case #%d: %s' % (count/2, solving(line.replace('\n', '')))
		count+=1