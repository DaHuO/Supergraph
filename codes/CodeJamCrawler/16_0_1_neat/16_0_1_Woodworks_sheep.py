import sys
import os

def count(fileIn, fileOut):
	f = open(fileIn,'r')
	t = int(f.readline())
	fTwo = open(fileOut,'w')
	for x in range(t):
		testCase = int(f.readline())
		if(testCase==0):
			fTwo.write("Case #"+str(x+1)+": INSOMNIA\n")
		else:
			a = [10,10,10,10,10,10,10,10,10,10]
			n = 1
			while 10 in a:
				num=testCase*n
				lst = [int(i) for i in str(num)]
				for i in range(len(lst)):
					a[lst[i]]=lst[i]
				n=n+1
			fTwo.write("Case #"+str(x+1)+": "+str(num)+"\n")
	f.close()
	fTwo.close()
def main():
	count('A-large.in','A-large.out')
	print(open('A-large.out','r').read())
if __name__ == '__main__':
	main()
