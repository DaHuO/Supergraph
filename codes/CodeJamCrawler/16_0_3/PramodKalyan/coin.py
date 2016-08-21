import itertools
import math
def checkprim(n):
    if n % 2 == 0 and n > 2: 
        return 0
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return i
    return 0
			
t = int(input())
for f in range(t):

	string = input()
	length,num = string.split()
	length = int(length)
	num = int(num)
	nooft=0;
	a = list(itertools.product('10',repeat=length))
	#print(a)
	fin=0
	div = []
	print("case #",end="")
	print(f+1,end="")
	print(":");

	for i in a:
		#print("hello")
		if(i[0]=='1' and i[len(i)-1]=='1') and nooft<num:
			#print("hell")
			s = "".join(i)
			fin=0
			#print(s)
			div=[]
			for k in range(2,11):
			
				n = int(s,k)
				#print(n)
				x = checkprim(n);
				#print(x)
				if(x != 0):
					div.append(x)
					fin = fin+1
			if(fin==9):
				nooft = nooft+1 
				print(s,end=" ")
				for i in div:
					print(i,end=" ")
				print()

					
				
       

