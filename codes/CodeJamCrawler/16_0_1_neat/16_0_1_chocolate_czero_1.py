outF = open("1b.out","w")

with open("1b.in","r") as inF:
    t= int(inF.readline())
    for it in xrange(t):
        print it,	
        n= int(inF.readline())
        
        if n==0:
			outF.write("Case #%d: %s\n"%(it+1,"INSOMNIA"))
			continue
		
        digits=[]
        i=1	
        flag=0		        
        while True:
			ans = i*n
			while ans:
				if not(ans%10 in digits):
					digits.append(ans%10)
				ans/=10
				if len(digits)==10:
					res = i*n
					flag=1
					break
			if flag:
				break
			i+=1
			
        outF.write("Case #%d: %d\n"%(it+1,res))

outF.close()
		
print "done"