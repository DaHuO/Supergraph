t = int(raw_input())
arr = ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']
dic = {'ZERO':0, 'ONE':1, 'TWO':2, 'THREE':3, 'FOUR':4, 'FIVE':5, 'SIX':6, 'SEVEN':7, 'EIGHT':8, 'NINE':9}
dic1 = {}
for x in xrange(1,t+1):
	array1 = []
	final = []
	string = raw_input()

	zero = string.count('Z')
	dic1['ZERO'] = zero
	two = string.count('W')
	dic1['TWO'] = two
	eight = string.count('G')
	dic1['EIGHT'] = eight
	three = string.count('H') - eight
	dic1['THREE'] = three 
	four = string.count('U')
	dic1['FOUR'] = four
	five = string.count('F') - four
	dic1['FIVE'] = five
	six = string.count('X')
	dic1['SIX'] = six
	seven = string.count('V') - five
	dic1['SEVEN'] = seven
	nine = string.count('I') - five - six - eight
	dic1['NINE'] = nine
	one = string.count('E') - zero - three*2 - five - seven*2 - eight - nine
	dic1['ONE'] = one

	for y in dic1:
		for z in xrange(0, dic1[y]):
			final.append(dic[y])
	# for y in string:
	# 	array1.append(y)
	# for z in arr:
	# 	for a in xrange(0, len(z)):
	# 		if z[a] in array1:
	# 			array1.remove(z[a])
	# 			found = 1
	# 			continue
	# 		else:
	# 			found = 0
	# 			break
	# 	if found == 1:
	# 		final.append(dic[z])
	# 		arr.append(z)
	# 	else:
	# 		for l in xrange(0, a+1):
	# 			array1.append(z[l])
	final.sort()
	# print final
	print "Case #{}:".format(x), 
	k = ""
	for n in final:
		k = k + str(n)
	print k