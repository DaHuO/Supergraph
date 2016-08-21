def findans(S):

	l = len(S)
	ans = S[0]
	if l == 1:
		return S

	for c in S[1:]:
		if c >= ans[0]:
			ans = c + ans
		else: 
			ans = ans + c


	print ans
	return ans
	


def main():
	t = int(raw_input())
	f = open('output.txt', 'w')

	for i in range(0,t):
		S = str(raw_input())
		ans = findans(S)
		f.write("Case #"+str(i+1)+": "+str(ans)+"\n")
	
	f.close()

if __name__ == "__main__":
    main()