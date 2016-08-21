
class Party():
	def __init__(self, name, num):
		self.name = name
		self.num = num

def evacuation(n, p):
	party_list = []
	party_name_list = []
	party_num_list = p
	res = []

	for i in range(n):
		party_name_list.append(chr(ord('A') + i))

	for i in xrange(n):
		party = Party(party_name_list[i], party_num_list[i])
		party_list.append(party)


	while party_list:
		party_list = sorted(party_list, key = lambda x: x.num)
		if len(party_list) > 3:
			if party_list[-1].num == party_list[-2].num:
				res.append(party_list[-1].name+party_list[-2].name)
				party_list[-1].num -= 1
				party_list[-2].num -= 1
				if party_list[-2].num <= 0:
					party_list.pop(-2)
				if party_list[-1].num <= 0:
					party_list.pop()
			else:
				res.append(party_list[-1].name)
				party_list[-1].num -= 1
				if party_list[-1].num <= 0:
					party_list.pop()
		elif len(party_list) == 3:
			res.append(party_list[-1].name)
			party_list[-1].num -= 1
			if party_list[-1].num <= 0:
				party_list.pop()
		else:
			if party_list[-1].num != party_list[-2].num:
				res.append(party_list[-1].name)
				party_list[-1].num -= 1
			else:
				res.append(party_list[-1].name+party_list[-2].name)
				party_list[-1].num -= 1
				party_list[-2].num -= 1
				if party_list[-1].num == 0:
					party_list.pop()
					party_list.pop()

	return res

t = int(raw_input())

for i in xrange(t):
	n = int(raw_input())
	p = [int(x) for x in raw_input().split()]

	print 'Case #%s: %s'%(i+1, ' '.join(evacuation(n, p)))




