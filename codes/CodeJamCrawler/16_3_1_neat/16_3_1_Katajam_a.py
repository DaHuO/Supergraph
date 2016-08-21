T_CASES = int(input())

def getOneTwo(data, total):
	ans = []
	while total > 1:
		sorted_data = sorted(data.items(), key = lambda x:x[1])
		if data[sorted_data[-1][0]] > total/2:
			cur_ans = sorted_data[-1][0]+sorted_data[-1][0]
			ans.append(cur_ans)
			data[sorted_data[-1][0]] -= 2
		else:
			cur_ans = sorted_data[-1][0]+sorted_data[-2][0]
			ans.append(cur_ans)
			# print(sorted_data)
			data[sorted_data[-1][0]] -= 1
			data[sorted_data[-2][0]] -= 1
		total -= 2

	if total == 1: 
		sorted_data = sorted(data.items(), key = lambda x:x[1])
		ans.insert(-1, sorted_data[-1][0])
	return ans



for i in range(T_CASES):
	N_PARTIES = int(input())
	SENATORS = [int(i) for i in input().split()]
	total = sum(SENATORS)
	# print(total)


	data = {}
	for x in range(N_PARTIES):
		data[chr(65+x)] = SENATORS[x]
	# print(data)
	ans = getOneTwo(data, total)
	# print(ans)



	print('Case #{}: {}'.format(i+1, ' '.join(ans)))

































