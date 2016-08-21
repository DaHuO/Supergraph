with open('input.in') as f:
	w = open('output.txt','w')
	mylist = f.read().splitlines() 
	print(mylist)
	for blah in range(0,int(mylist[0])):
		indexes = ['1']
		K,C,S = [int(s) for s in mylist[blah+1].split()]
		if(S < K): 
			w.write("Case #{}: IMPOSSIBLE\n".format(blah+1))
		else:
			for i in range(2,K+1):
				index = i
				for j in range(1,C):
					index += pow(K,j)
				indexes.append(str(index))
			
			w.write("Case #{}: {}\n".format(blah+1,  ' '.join(indexes[:S])))