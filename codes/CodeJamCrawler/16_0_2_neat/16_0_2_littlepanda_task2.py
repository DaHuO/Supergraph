def f(x):
	if x == '+':
		return '-';
	else:
		return '+';
	
def invert(l):
	return [f(x) for x in l];

def solve(l, ans):
	while (l) and (l[-1] == '+'):
		l.pop();
	if not l:
		return ans;
	else:
		return solve(invert(l), ans+1);

def main():
	fin = open('input','r');
	fout = open('output','w');
	
	tt = int(fin.readline());
	for i in range(1,tt+1):
		s = fin.readline();
		l = list(s);
		fout.write('Case #'+str(i)+': '+ str(solve(l[:-1],0)) +'\n');
			
if __name__ == '__main__':
	main();
	