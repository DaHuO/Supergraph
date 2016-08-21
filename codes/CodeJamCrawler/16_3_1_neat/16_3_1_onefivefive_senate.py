def solve(N,P):
	ch='A'
	data=[]
	total=0
	for i in range(N):
		data.append((0-P[i],ch))
		ch=chr(ord(ch)+1)
		total=total+P[i]
	from heapq import heapify, heappop,heappush
	heapify(data)
	print(data)
	print(total)
	result=[]
	while len(data)>0:
		x=heappop(data)
		total=total-1
		if total==0:
			result.append(x[1])
			break
		if x[0]+1<0:
			heappush(data,(x[0]+1,x[1]))
		y=heappop(data)
		total=total-1
		if total==0:
			result.append(x[1]+y[1])
			break
		if (0-data[0][0])>(0-y[0]-1) and (0-data[0][0])>total//2:
			result.append(x[1])
			heappush(data,y)
			total=total+1
		else:
			result.append(x[1]+y[1])
			if y[0]+1<0:
				heappush(data,(y[0]+1,y[1]))
	return result
def senate(inputfile, outputfile):
	fr=open(inputfile,'r')
	T=int(fr.readline())
	fw=open(outputfile,'w')
	for j in range(T):
		N=int(fr.readline())
		P=[int(s) for s in fr.readline().split(" ")]
		result=solve(N,P)
		s='Case #'+str(j+1)+':'
		for s1 in result:
			s=s+' '+s1
		s=s+'\n'
		fw.write(s)
	fw.close()
	fr.close()
	return
