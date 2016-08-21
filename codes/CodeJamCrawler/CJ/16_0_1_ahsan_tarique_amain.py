l = [0,0,0,0,0,0,0,0,0,0]

def resetl():
	for i in range(10):
		l[i]=0
	return

def checkl():
	for i in range(10):
		if(l[i]==0):
			return False;
	return True;

def checknumber(x):
	while(x != 0):
		mod = int(x%10)
		l[mod] = 1
		x = int(x/10)

def ans(x):
	resetl()
	if(x ==0):
		return "INSOMNIA"

	i = 0;
	while(checkl()==False):
		i+=1
		checknumber(i*x)

	return i*x


def main():

	test = int(input())
	for t in range(1,test+1):
		n = int(input())
		v = ans(n)
		print("Case #{}: {}".format(t,v))

	return


main()
