
def sol(N):
	if(N==0):
		return "INSOMNIA"
	num=0
	bool=[False]*10
	while all(bool)==False:
		num += N
		m=len(str(num))
		a=[0]*m
		for i in range(m):
			a[i]=int(str(num)[i])
		for i in range(m):	
			bool[a[i]]=True
	return num	
			
def main():
	T = int(input())
	for i in range(T):
		N = int(input())
		y = sol(N)
		print("Case #{}: {}".format (i+1, y))
	
	
if __name__ == "__main__": main()