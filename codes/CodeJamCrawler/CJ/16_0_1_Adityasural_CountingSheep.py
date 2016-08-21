import sys
if __name__ == "__main__":
	f = sys.stdin
	if len(sys.argv) >= 2:
		fn = sys.argv[1]
		if fn != '-':
			f = open(fn)
	t = int(f.readline())
	for _t in range(t):
		a=int(f.readline())
		b=0
		if(a!=0):
			count=0
			arrToFill=[0,0,0,0,0,0,0,0,0,0]
			while(count<10):
				b=b+a
				j=0
				for j in range(0, 10):
					if (arrToFill[j]==0):
						if(str(j) in str(b)):
							arrToFill[j]=arrToFill[j]+1
							count=count+1
			print("Case #{}: {}".format(_t+1, b))
		else:
			print("Case #{}: INSOMNIA".format(_t+1))