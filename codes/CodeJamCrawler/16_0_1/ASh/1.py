#!usr/bin/python

from scipy import loadtxt

f=loadtxt("A-large.in", unpack=True)
g=open("output1.dat", "w")

def integer(a):
	ans=[]
	while a/10 != 0.0:
		ans.append(a%10)
		a=a/10
	ans.append(a)
	return ans	

T=f[0]
data=f[1:]
i=0

while i<len(data):
	N=int(data[i])
	numbers=[0,1,2,3,4,5,6,7,8,9]
	history=[]
	j=1
	while len(numbers)>0:
		n=N*j
		#print n
		if history.count(n)==1:
			print>>g, "Case #"+str(i+1)+": INSOMNIA"
			break
		history.append(n)	
		integers=integer(n)
		for each in integers:
			if numbers.count(each)==1:
				numbers.remove(each)
		
		if len(numbers)==0:
			print >>g,"Case #"+str(i+1)+": "+str(n)
			break
		j+=1
	i+=1
	
		
