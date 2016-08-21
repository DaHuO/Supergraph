

test_cases=int(raw_input())
cases = 1
while cases <= test_cases :
	N = int(raw_input())
	a = [1,2,3,4,5,6,7,8,9,0]
	i=1
	if N == 0 :
		 print 'Case #'+str(cases) + ': INSOMNIA'
	else :
		while a.__len__() != 0  :
			m = i*N
			m =str(m)
			m_split = map(int,str(m))
			for x in m_split :
				if a.__contains__(x):
					a.remove(x)
				if a.__len__() == 0 :
					print 'Case #'+str(cases) + ': '+ m
					break	 
			i+=1
	cases+=1	
		
