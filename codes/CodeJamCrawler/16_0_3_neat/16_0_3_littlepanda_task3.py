from math import *;
fout = open('output','w');	

def divisor(n):
	for j in range(2, ceil( sqrt(n) ) + 1):
		if (n % j == 0):
			return j;
	return 1;

def solve(n):
	s = bin(n)[2:];
	
	l = [];
	for b in range(2,11):
		d = divisor(int(s,b));
		if ( d != 1 ):
			l.append( str(d) );
		else:
			return False;
	
	fout.write(s + ' ' + ' '.join(l)+'\n');
	return True;
		
def main():
	fout.write('Case #1:\n');
	
	ans = 0;
	
	i = 32769;
	
	while (ans < 50):
		if ( solve(i) ):
			ans += 1;
		i += 2;
			
if __name__ == '__main__':
	main();