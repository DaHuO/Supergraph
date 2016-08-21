import itertools
test=input()
w=test
final=[]
fin=[]
def is_prime(a):
	a=long(a)
	i=0
	i=long(i)
	for i in range(2,a):
		if (a % i) == 0:
			return False,long(a//i)
			break	
	else:
		return True,0

while test != 0:
	flag=0
	
	N,J=map(int,raw_input().split())
	array=[]
	lst = map(list, itertools.product([0, 1], repeat=N))
	for i in lst:
		temp=''
		for m in i:
			if(i[0]==1 and i[-1]==1):
				temp+=str(m)
		if(i[0]==1 and i[-1]==1):
			array.append(temp)
	

	for m in array:
		temp1=[]
		u=long(m,2)
		boole,temp2=is_prime(u)
		if boole==False:
			for ii in range(2,11):
				
				u=long(m,ii)
				for ik in [2,3,5,7,11,13,17,19,23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103]:
					if(u%ik) ==0:
						temp2=u//ik
						temp1.append(temp2)
						break
		if(len(temp1)==9):
			flag=1
		else:
			flag=0
		if(flag==1):
			final.append(m)
			fin.append(temp1)
		if(len(final) == J):
			break
	print "Case #"+str(w-test + 1)+":"
	
	number=0
	for k in final:
		print k ,' '.join(map(str, fin[number]))
		number+=1
			
	test-=1
