from math import sqrt
def isntprime(num):
	for i in xrange(2,int(sqrt(num))+1):
		if num % i == 0 :
			return True
	return False
def check(coin):
	boo = True
	for i in xrange(2,11):
		boo = boo and isntprime(int(coin,i))
	return boo
def find_div(num):
	for i in xrange(2,int(sqrt(num))+1):
		if num % i == 0 :
			return i
def fin_all_div(string):
	output=[]
	for i in xrange(2,11):
		output.append(str(find_div(int(string,i))))
	return output
def coin(leng,n,f):
	t=0
	output=''
	for i in xrange(2**(leng-2)):
		s='1{:0>{}}1'.format(bin(i)[2:],leng-2)
		if check(s):
			if t==n:
				return
			t+=1
			f.write('{} {}\n'.format(s,' '.join(fin_all_div(s))))
leng,n=0,0
with open('C-small-attempt0.in','r') as f:
	q=f.readlines()
	leng=int(q[1].split(' ')[0])
	n=int(q[1].split(' ')[1])
with open('tempo_google.txt','w') as f:
	f.write('Case #1:\n')
	coin(leng,n,f)
			
