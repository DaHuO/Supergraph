import itertools

def matriz(l,N):
	l = sorted(l)
	m = list(itertools.combinations(l,N))
	for mm in m:
		lista = list(mm)
		t = [list(i) for i in zip(*lista)]
		lv = l
		rowcol = lista + t
		res = []
		for i in rowcol:
			if sorted(i) == i and i in lv:
				idx = lv.index(i)
				lv = lv[:idx] + lv[idx+1 :]
				res.append(True)
			else:
				res.append(False)
		if res.count(False) == 1:
			print ' '.join(map(str,(lista + t)[res.index(False)]))
			break	

		




if __name__ == '__main__':
	T = int(raw_input())
        for i in range(0,T):
		N = int(raw_input())
		lista = []
		st =  'Case #'+str(i+1)+':'
		print st,
		for n in range(0,(2*N)-1):	
                	linha = raw_input()
                	l = map(int,linha.split())
			lista.append(l)
		matriz(lista,N)

