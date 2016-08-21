import sys
import os

def compose(k,c):
	length = k**c
	#there are length total tiles
	#a pattern is included in every set of k**(c-1) tiles
	tiles=[]
	additive = k**(c-1)
	for x in range(0,k):
		tiles.append(str(1+x*additive))
	return tiles
def main():
	f = open('D-small-attempt0.in','r')
	fTwo = open('gold.out','w')
	t = int(f.readline())
	for x in range(t):
		kcs = f.readline().split(' ')
		k = kcs[0]
		c = kcs[1]
		s = kcs[2]
		tiles = ' '.join(compose(int(k),int(c)))
		fTwo.write('Case #'+str(x+1)+': '+tiles+'\n')
	f.close()
	fTwo.close()
	print(open('gold.out','r').read())
if __name__=='__main__':
	main()
