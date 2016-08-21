import math
def is_prime(n):
	for i in range(2,int(math.sqrt(n)+1)):
		if (n%i==0):
			return n/i
	return -1
	
file = open('C-small-attempt0.in', 'r')
ip=file.readlines()
T=int(ip[0]);
line_no=1
while (T):
	dump=ip[line_no]
	N=int((ip[line_no].split(" "))[0])
	J=int((ip[line_no].split(" "))[1])
	print N,J
	s="1"*N
	p= int(s,2)
	hey=0;
	print "Case #"+str(line_no)+":"
	for i in range(p+1):
		if(hey!=J):
			s= "{0:b}".format(i)
			#print N, len (s), s, s[0], s[-1]
			if (len(s)==N and s[0]=='1' and s[-1]=='1'):
				#print s
				flag_any_prime=0
				list_k=[]
				for i in range(2,11):
					num_base=int(s,i)
					list_k.append(is_prime(num_base))
				if (-1 not in list_k):
					print s,
					for i in list_k:
						print i,
					print
					hey+=1		
		else:
			break
	line_no+=1
	T-=1
