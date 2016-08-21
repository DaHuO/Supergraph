# def squad(n,k):
# 	if n<k:
# 		return 0
# 	if n<2*k:
# 		return 1
# 	result=1
# 	for i in range(k,n):
# 		result=result+squad(n-i,i)

# 	return result

# print squad(10,3)

################################################################

# from interviewbit.graph import Graph
# from interviewbit.queue import Queue

# g=Graph()
# g.addEdge('a','d')
# g.addEdge('f','b')
# g.addEdge('b','d')
# g.addEdge('f','a')
# g.addEdge('d','c')


# l=g.getVertex('f').getConnections()
# for i in l:
# 	print i.id

#####################################################################


# words=['This', 'is', 'an', 'example', 'of', 'text', 'justification.']
# L=16

# j=0
# i=0
# while i<len(words):
# 	temp_len=L
# 	while temp_len>=0 and i<len(words):
# 		temp_len-=(len(words[i])+1)
# 		if temp_len>=0:
# 			i+=1
# 	print words[j:i]
# 	j=i

###########################################################################

# def permutation(j,row,col,first,output):
# 	for i in range(row):
# 		output[j]=first[j][i]

# 		if j<col-1:
# 			permutation(j+1,row,col,first,output)

# 		if j==col-1:
# 			for k in range(col):
# 				print output[k],
# 			print


# l=[[1,2,3],
#    [4,5,6],
#    [7,8,9]]
# output=[None]*3
# permutation(0,3,3,l,output)

##########################################################################

# def isprime(n):
# 	'''check if integer n is a prime'''
# 	# make sure n is a positive integer
# 	n = abs(int(n))
# 	# 0 and 1 are not primes
# 	if n < 2:
# 		return False
# 	# 2 is the only even prime number
# 	if n == 2: 
# 		return True    
# 	# all other even numbers are not primes
# 	if not n & 1: 
# 		return False
# 	# range starts with 3 and only needs to go up the squareroot of n
# 	# for all odd numbers
# 	for x in range(3, int(n**0.5)+1, 2):
# 		if n % x == 0:
# 			return False
# 	return True


# def factors(n):    
# 	return set(reduce(list.__add__, 
# 				([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

# def toStr(n,base):
# 	convertString = "0123456789"
# 	if n < base:
# 		return convertString[n]
# 	else:
# 		return toStr(n//base,base) + convertString[n%base]


# def generate(n):
# 	p=[]
# 	q=[]
# 	jamcoin=[]
# 	for i in xrange(1<<n):
# 		l=[]
# 		for j in xrange(n):
# 			if i&(1<<j):
# 				l.append('1')
# 			else:
# 				l.append('0')
# 		p.append(l)
	
# 	for i in p:
# 		if i[0]=='1' and i[-1]=='1':
# 			q.append(''.join(i))

# 	for i in q:
# 		for j in [2,3,4,5,6,7,8,9,10]:
# 			converted=toStr(int(i),j)
# 			if isprime(converted):
# 				break
# 		jamcoin.append(i)

# 	print jamcoin

# print generate(6)

################################################################

# from interviewbit.graph import Graph
# from interviewbit.queue import Queue

# def flip(string):
# 	l=[]
# 	for i in range(1,len(string)+1):
# 		temp=''
# 		temp=string[:i][::-1]
# 		rem=string[i:]
# 		list_temp=list(temp)
# 		for i in range(len(list_temp)):
# 			if list_temp[i]=='-':
# 				list_temp[i]='+'
# 			else:
# 				list_temp[i]='-'
# 		temp=''.join(list_temp)+rem
# 		l.append(temp)
# 	return l


# def pancakes(string,target):
# 	# if all(i=='+' for i in string):
# 	# 	return string
# 	# else:
# 	# 	p=flip(string)
# 	# 	for i in p:
# 	# 		return pancakes(i)

# 	done=[]
# 	p=[]
# 	g=Graph()
# 	q=[string]
# 	right=True
# 	while right:
# 		current=q.pop()
# 		done.append(current)
# 		p=flip(current)
# 		for i in p:
# 			if i!=target:
# 				if not i in done:
# 					g.addEdge(current,i)
# 			elif i==target:
# 				g.addEdge(current,i)
# 				right=False
# 			else:
# 				continue

# 			q.insert(0,i)

# 	return g


# def BFS(g,start):  # g is the graph and start is the starting vertex
# 	start.setDistance(0)
# 	start.setPredecessor(None)
# 	verticesQueue=Queue()
# 	verticesQueue.enqueue(start)
# 	while verticesQueue.size()>0:
# 		currentVertex=verticesQueue.dequeue()
# 		for nbr in currentVertex.getConnections():
# 			if nbr.getColor()=='white':
# 				nbr.setColor('gray')
# 				nbr.setDistance(currentVertex.getDistance()+1)
# 				nbr.setPredecessor(currentVertex)
# 				verticesQueue.enqueue(nbr)
# 		currentVertex.setColor('black')

# t=input()
# count=1
# output=[]
# while t>0:
# 	string=raw_input()
# 	target=string.replace('-','+')
# 	# print flip(string)
# 	graph=pancakes(string,target)
# 	start=graph.getVertex(string)
# 	BFS(graph,start)

# 	def traverse(y):
# 		x=y
# 		output.append('Case #'+str(count)+': '+str(x.getDistance()))
# 	traverse(graph.getVertex(target))
# 	count+=1
# 	t-=1

# for i in output:
# 	print i

#######################################################################

def pancakes(string):
	if all(i=='+' for i in string):
		return 0
	elif string[0]=='-' and string[-1]=='-':
		return len(string)
	elif string[0]=='-' and string[-1]=='+':
		return len(string)-1
	elif string[0]=='+' and string[-1]=='-':
		return len(string)
	elif string[0]=='+' and string[-1]=='+':
		return len(string)-1

t=input()
count=1
output=[]
while t>0:
	string=raw_input()
	output.append('Case #'+str(count)+': '+str(pancakes(string)))
	t-=1
	count+=1

for i in output:
	print i




