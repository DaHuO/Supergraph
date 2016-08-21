
def ok(d):
	for x in range(0,10):
		if not d[str(x)]:
			return False;
	return True;

def main():
	fin = open('input','r');
	fout = open('output','w');

	tt = int(fin.readline());
	for i in range(1,tt+1):
		n = int(fin.readline());
		if (n == 0):
			fout.write('Case #'+str(i)+': INSOMNIA\n');
		else:
			d = { str(x) : False for x in range(0,10) };
			for letter in str(n):
				d[letter] = True;
			num = n
			cur = 1
			while not ok(d):
				cur = cur + 1;
				num = n*cur;
				for letter in str(num):
					d[letter] = True;
			fout.write('Case #'+str(i)+': '+str(num)+'\n');
			
if __name__ == '__main__':
	main();