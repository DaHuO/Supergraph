def findans(arr):
	ans = 0
	l = len(arr)
	minus = 0

	if l == 1:
		return 0 if arr[0] == '+' else 1

	if arr == l*'-':
		return 1

	for j in range(1, l):
		if arr[j-1] == '+' and arr[j] == '-':
			ans = ans + 2
			minus = 1
		elif arr[j-1] == '-' and arr[j] == '+':	
			if minus == 0:
				ans = ans + 1
			else: 
				minus = 1

	return ans


def main():
	N = int(raw_input())
	f = open('output.txt', 'w')

	for i in range(0,N):
		arr = raw_input().split()
		ans = findans(arr[0])
		f.write("Case #"+str(i+1)+": "+str(ans)+"\n")
	
	f.close()

if __name__ == "__main__":
    main()