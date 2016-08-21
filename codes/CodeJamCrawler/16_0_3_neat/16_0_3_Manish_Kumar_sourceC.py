import itertools
import math
def isprime(n):
    for m in range(2, int(n**0.5)+1):
        if not n%m:
            return False
    return True
h=open("C-small-attempt2.in","r")
o=open("output.txt","a")
f=h.readlines()
w=f[1].split()
n=int(w[0])
z=int(w[1])
x=['0']*n
st=[0]*9
x[0]='1'
x[n-1]='1'
s=0
e=0
count=0
q=["".join(seq) for seq in itertools.product("01", repeat=(n-2))]
o.write("Case #1:\n")
for a in range(0,len(q)):
	x[1:n-1]=[c for c in q[a]]
	num=[''.join(x[0:])]
	for i in range(2,11):
		s=0
		for j in range(0,n):
			try:
				s=long(s+(long(x[n-1-j])*math.pow(i,j)))
			except:
				e=1
				break
		if e==1:
			break
		if isprime(s)==True:
			break;
		else:
			for m in range(2,long(s**0.5)+1):
				if s%m==0:
					st[i-2]=m
					break
		if i==10:
			count=count+1
			o.write(num[0]+" ")
			for i in range(0,9):
				o.write(str(st[i])+" ")
				if i==8:
					o.write("\n")
			if count==z:
				exit()