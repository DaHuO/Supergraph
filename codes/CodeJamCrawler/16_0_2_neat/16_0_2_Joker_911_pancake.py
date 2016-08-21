def lastchr(ts):
	
	if not len(ts)==0:
		if ts[len(ts)-1]=='+':
			return lastchr(ts[:-1])
		else: return ts
def reduce(st):
	li=list()
	j=0
	li.append(st[0])
	for i in range(len(st)):
		if not li[j]==st[i]:
			li.append(st[i])
			j+=1
	return li




with open('B-large.in','r') as f:
	x=int(f.readline())
	for i in range(x):
		st=f.readline()
		tot=0
		st=st[:-1]
		

		
		ts=reduce(st)	
		ts=lastchr(ts)

		if not ts is None:
			if not len(ts)%2==0:
				tot+=1
				ts=ts[:-1]
			if not ts is None:	
				if len(ts)>0:
					tot+=len(ts)
				
			print("Case #"+str(i+1)+":"+" "+str(tot))
		else:
			print("Case #"+str(i+1)+":"+" "+str(0))

			
		

		
		


		#	
#
#				if ts[0]=='-':
#					tot+=1
#				ts=ts[1:]
		
			#if len(ts)>0:
				#for j in range(0,len(ts),2):
					#if ts[j]=='+' and ts[j+1]=='-':
						#tot+=2
					#elif ts[j]=='-' and ts[j+1]=='+':
						#tot+=1
					#elif ts[j]=='-' and ts[j+1]=='-' and j==0:
						#tot+=1
					
		#print("Case #"+str(i+1)+":"+" "+str(tot))'''
		



		

