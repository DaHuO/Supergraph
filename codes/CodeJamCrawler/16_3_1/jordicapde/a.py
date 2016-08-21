from string import letters
T = int(input())

for t in range(1, T + 1):
	N = int(input())
	P = [int(s) for s in raw_input().split(" ")]
	res = []
	finish = False
	
	while not finish:
		max_p = max(P)
		index_max = P.index(max_p)
		
		P_aux = P[:]
		count = 2
		if max_p < 2:
			count = 1
			
		P_aux[index_max] -= count
		
		if max(P_aux) <= sum(P_aux) / 2:
			P = P_aux[:]
			res += [letters[index_max] * count]
			
		else:
			P_aux = P[:]
			P_aux[index_max] -= 1
			index_max2 = P_aux.index(max(P_aux))
			P_aux[index_max2] -= 1
			
			if max(P_aux) <= sum(P_aux) / 2:
				P = P_aux[:]
				res += [letters[index_max] + letters[index_max2]]
			else:
				P_aux[index_max2] += 1
				P = P_aux[:]
				res += [letters[index_max]]
				
		finish = all([p == 0 for p in P])
				
			
	res = " ".join(res).upper()
	print("Case #{}: {}".format(t, res))
	
