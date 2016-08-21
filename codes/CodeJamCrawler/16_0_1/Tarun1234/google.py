x=input()
count1=1
for t in range(0,x):
    num=input()
    if(num==0):
        print "Case #"+str(count1)+": " + str("INSOMNIA")
        count1=count1+1
    else:
    	list=[]
    	count=1
    	while(1):
    		d=num*count
    		while(1):
    			b=d/10
    			c=d%10
    			if(b==0 and c==0):
    				break
    			else:
    				if c not in list:
    					list.append(c)
    			d=b
    		if(len(list)==10):
    			break
    		count=count+1
    	print "Case #"+str(count1)+": " + str(num*count)
    	count1=count1+1