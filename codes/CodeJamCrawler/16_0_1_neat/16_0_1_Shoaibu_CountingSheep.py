digits = list(range(0,10))

def digitize(N):
	arr = [int(i) for i in str(N)]
	return arr

def check(N,temp,c):
	if N == 0:
		return "INSOMNIA"
	elif (set(temp) == set(digits)):
		return c*N
	else:
		c=c+1
		newN = c*N
		temp2 = digitize(newN)
		for i in temp2:
			if(i not in temp):
				temp.append(i)
		return check(N,temp,c)


def Count(N):
	temp = digitize(N)
	ans = check(N,temp,1)
	return ans

def main():
	outFile = open('A-large-output.txt','w')
	with open ('A-large.in', 'r') as f:
		arr = []
		i=0
		line = f.readline()
		l = int(line)
		for i in range(1,l+1):
			line = int(f.readline())
			outFile.write("Case #"+str(i)+":" +' '+ str(Count(line))+'\n')



if __name__ == '__main__':
	main()