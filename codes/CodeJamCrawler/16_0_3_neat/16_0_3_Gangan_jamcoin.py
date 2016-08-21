import math
cases = int(input())

def find_div(n, limit=4069):
	if(n%2==0): return 2;
	if(n%3==0): return 3;
	i=5
	k = int(n**.5)
	while(i<=limit and i<=k):
		if(n%i==0):return i
		if(n%(i+2)==0):return i+2
		i+=6
	return 0
def convert(coin,base):
	coin=coin[::-1]
	b=1
	sum=0
	for i in range(len(coin)):
		if coin[i]=="1":
			sum+=base**i
	return sum

for case in range(cases):
	print("Case #"+str(case+1)+":")
	(size, amount) = [int(i) for i in input().split(" ")]
	pcoins=[]
	z=0
	rng = 2**(size-2)
	temp = bin(z)[2::]
	temp= "0"*(size-2-len(temp)) + temp
	pcoins.append("1"+temp+"1")
	r = 0
	pi=0
	while pi < len(pcoins):
		p=pcoins[pi]
		pi+=1
		z+=1
		if(z<rng):
			temp = bin(z)[2::]
			temp= "0"*(size-2-len(temp)) + temp
			pcoins.append("1"+temp+"1")	
		divs = []
		for b in range(2,11):
			a=find_div(convert(p,b))
			if(a):
				divs.append(a)
			else:
				break
		if(len(divs)==9):
			print(p+" "+" ".join([str(x) for x in divs]))
			r+=1
		if r>=amount:
			break