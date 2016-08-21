#!/usr/bin/python
import sys

def main():
	t = int(sys.stdin.readline())
	j = 1
	while t > 0 :
		t -= 1
		ans = 0
		st = sys.stdin.readline()
		i = 0
		flag = 0
		
		for x in st:
			if x == '+' :
				flag = 1
			if x == '-' and flag:
				flag = 0
				ans += 2
			if x == '-' and i == 0 :
				ans += 1
				
			i += 1
		print("Case #"+str(j)+": "+str(ans))
		j += 1
	return 0
if __name__=='__main__':
	main()

