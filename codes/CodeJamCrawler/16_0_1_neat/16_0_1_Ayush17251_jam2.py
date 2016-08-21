#f = open('A-small-attempt5.in', 'r')
#f1=f.readlines()

m=input()
b=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
def check(c):
	while(c!=0):
		q=c%10
		if  q not in d:
			d.append(q)
		c=c/10		
	return d
	
#f2 = open("Jam1_output1.txt", "w")				
for i in range(1,m+1):
	d=[]
	a=input()
	c=0
	flag=0
	for j in range(1,200):
		c=j*a
		check(c)
		d=sorted(d)
		x=cmp(b,d)
		if x==0:
			print("Case #"+str(i)+": "+str(c))
			flag=1
			break				
	if flag==0:
		print("Case #"+str(i)+": INSOMNIA")	
			
	
#f.close()
#f2.close()			
			
			
			
			
			

