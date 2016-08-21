import sys
import os
import random

def check(coin,base):
	digits = list(coin)
	digits.reverse()
	n=0
	total=0
	print('[*] Testing '+coin)
	for x in digits:
		if(x=='1'):
			total = total+(base**n)
		n=n+1
	print('\t[*] Converted to base '+str(base))
	for x in range(2,21):
		if(total % x ==0):
			return x
	return 0
def checkAllBases(pattern):
	for x in range(2,11):
		if(check(pattern,x)==0):
			return False
	return True
def makeCoin(n):
	lst=['1','1']
	for x in range(n-2):
		lst.insert(1,str(random.randrange(0,2)))
	while(checkAllBases(''.join(lst))==False):
		lst=['1','1']
		for x in range(n-2):
			lst.insert(1,str(random.randrange(0,2)))
	return ''.join(lst)
def main():
	f=open('coinjam.in','r')
	f.readline()
	nj = f.readline().split(' ')
	n=nj[0]
	j=nj[1]
	fTwo=open('coinjam.out','w')
	fTwo.write('Case #1:\n')
	coins = []
	coin=makeCoin(int(n))
	for x in range(int(j)):
		while(coin in coins):
			coin=makeCoin(int(n))
		coins.append(coin)
		line=coin+' '
		print('[+] Chose coin '+coin)
		for bse in range(2,11):
			line+=str(check(coin,bse))+' '
		fTwo.write(line+'\n')
		print('[+] Made coins: '+str(len(coins)))
	f.close()
	fTwo.close()
	print(open('coinjam.out','r').read())
if __name__ == '__main__':
	main()
