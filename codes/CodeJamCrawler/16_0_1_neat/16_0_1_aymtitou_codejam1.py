
# 
test =  0 
k=0

import sys
with open('input', 'r') as test_cases:

	for line in test_cases:  
		if test ==0 :
			t = int(line) 
			test = 1	
		else:
			t  = t-1
			val = int (line)
			k = k+1
			list = [str(x) for x in range(10)]
			if val == 0 :
				res = 'INSOMNIA'	 
	
			else :
				N = val
				n = 1
				while True :
					for j in str(N) :
						if j in list:
							del list[list.index(j)] 
					if len(list)== 0: 
						res = N
						break 
					n=n+1
					N = val * n
									
			
			print "Case #{0}: {1}".format(k,res)


		if t==0 : 
			break  

#INSOMNIA
#Case #2: 10
#Case #3: 90
#Case #4: 110
#Case #5: 5076