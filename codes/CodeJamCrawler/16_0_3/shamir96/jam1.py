import math
input()
input()

l=16
R={}
g=0
def iscomp(num):
	if num > 1:
	# check for factors
		for i in range(2,int(math.sqrt(num))):
	    		if (num % i) == 0:
	    		    return i
	    		    break
		return False
def generate(n):
	for i in range(1, 2**n-1):
 	   yield '{:0{n}b}'.format(i, n=n)
#values=opt(l)#values is the list of l-bit strings

#compute gives the number and factor if composite
def compute(s):
	results={}
	for x in range(2,11):
		val=0
		for y in range(len(s)):
			val=val+int(s[y])*(x**(len(s)-y-1))
		if(iscomp(val)==False):
			return False
		results[val]=iscomp(val)
	return results
d={}
check={}

#for r in range(2**(l-2)):
#	check[values[r]]=compute(values[r])
	
#[print(x,check[x]) for x in check if check[x]]

  #opt gives the list of strings
def opt(l):
	g=0
	options=[]
	for x in generate(l-2):
		if g>=50:
			break
		z = compute("1"+x+"1")
		if(z):
			g=g+1
			d["1"+x+"1"]=z
	options.append("1"*l)
	options.append("1"+"0"*(l-2)+"1")
	return d 	

d=opt(l)
print("Case #1: ")
for k in d:
	print(k," ".join([str(d[k][j]) for j in sorted(d[k])]))
		

