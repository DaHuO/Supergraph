from __future__ import print_function
bit = [0]*37
prime =[2,3,5,7,11,13]
ans = [0]*11
def func(x):
	global bit
	ct=0
	while(x!=0):
		bit[ct]=x%2
		ct=ct+1
		x/=2

def func2(x):
	global ans
	num=0
	p=1
	for i in range (0,32):
		num = num + bit[i]*p
		p*=x

	for i in range (0,6):
		if(num%prime[i]==0):
			ans[x]=prime[i]
			return 1

	return 0

def main():
	global bit
	global prime
	global ans
	cnt=0
	i = (1<<31) + 1
	print ("Case #1:")
	while (cnt!=500):
		for j in range (0,36):
			bit[j]=0
		func(i)
		ct=0
		for j in range (2,11):
			ct = ct + func2(j)
		if (ct==9):
			for j in range (31,-1,-1):
				print (bit[j],end="")
			for j in range (2,11):
				print (" ",end="")
				print (ans[j],end="")
			cnt=cnt+1
			print ()
		i=i+2

if __name__ == '__main__':
    main()