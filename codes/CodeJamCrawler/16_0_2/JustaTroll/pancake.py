t = int(input()) 

def fufu(n):
	count  = 0
	size = len(n)
	l = []
	flag = 0
	for i in range(0,size):
		l.append(n[i])
	#print (l)
	for i in range(1,size):
		if (l[i]!=l[i-1]):
			count = count +1
			if (l[i-1]=='+'):
				for j in range(0,i):
					l[j]='-'
			else:
				for j in range(0,i):
					l[j]='+'
		if (i==size-1):
			if (l[i]=='-'):
				count = count+1
				#for j in range(0,i+1):
				#	l[j]='+'
	
	if (size==1):
		if l[0]=='-':
			return 1
	return count




for i in range(1, t+1):
  s = input()
  #print (s)
  print ("Case #{}: {} ".format(i, fufu(s)))