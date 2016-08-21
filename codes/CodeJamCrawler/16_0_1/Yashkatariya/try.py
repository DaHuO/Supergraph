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

def sheep(n):
	p=[None]*10
	if n==0:
		return 'INSOMNIA'
	for i in xrange(1,200):
		prod=i*n
		prod=str(prod)
		for i in range(len(prod)):
			if p[int(prod[i])]=='True':
				continue
			else:
				p[int(prod[i])]='True'

		if None in p:
			continue
		else:
			return prod
			break

l=[]
t=input()
count=1
while t>0:
	n=input()
	output=sheep(n)
	l.append('Case #'+str(count)+': '+output)
	t-=1
	count+=1

for i in l:
	print i










