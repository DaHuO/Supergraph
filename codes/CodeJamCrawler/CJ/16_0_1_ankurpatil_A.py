'''
Created on Apr 11, 2015

@author: Ankur Patil
'''
import sys
def main(infile, outfile):
	with open(infile,"rt") as f:
		T = int(f.readline())
		sol = []
		for t in range(1,T+1):
			ans = 0
			N = int(f.readline())
			cnt = 1
			occured = 0b0000000000
			while cnt < 100:
				number = N * cnt
				for l in str(number):
					occured = occured | int("1"+"0"*(int(l)),2)
					if occured == 0b1111111111:
						break;
				else:
					cnt = cnt + 1
					continue;
				ans = N * cnt
				break;
			else:
				ans = "INSOMNIA"
			sol.append("Case #{0}: {1}\n".format(t,ans))
		print(sol)
	with open(outfile, "wt") as f:
		f.writelines(sol)

if __name__ == '__main__':
	main(sys.argv[1],sys.argv[2])