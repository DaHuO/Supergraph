nt  = input()
digits = {'0', '1' , '2' , '3', '4' , '5' ,'6', '7', '8', '9'}
for x in range(1, nt+1):
        n = input() 
	j = n
        i = 1
	a = {}
	if n == 0:
        	print 'Case #'+str(x)+': INSOMNIA'
	else:
		while True:
			if digits == a:
	   			break;
			else:
            			n = j*i
            			a = set(a).union(list(str(n)))
        		#time.sleep(2)
			i = i+1
		print 'Case #'+str(x)+': '+str(n)
      
