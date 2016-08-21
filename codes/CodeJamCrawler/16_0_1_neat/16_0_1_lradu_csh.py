f = open('A-large.in', 'r')
g = open('countsh.out', 'w')

t=int(f.readline())
for i in range(0,t):
    n=int(f.readline())
    if n==0 :
		g.write('Case #%s: INSOMNIA' % (i+1) +'\n')
		continue
    l=[0]*10;
    x=0
    c=0
    while(x<10):
    	c+=1
    	for j in str((n*c)):
    		if l[int(j)]==0:
    			l[int(j)]=1
    			x+=1
     
     
    g.write('Case #%s:' % (i+1) +' '+ str(n*c)+'\n')
	
