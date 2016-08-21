def solve():
	N = int(input())
	P = [int(i) for i in input().split(" ")]
	result = ""
	
	while max(P) != 0:
		tmp = ""
		for x in range(2):
			maxi = max(P)
			if maxi == 0:
				break
			imax = [i for i, j in enumerate(P) if j == maxi]
			tmp += chr(imax[0] + 65)
			P[imax[0]] -= 1
			
		maxi = max(P)
		imax = [i for i, j in enumerate(P) if j == maxi]
		if maxi == 1 and len(imax) == 1:
			P[imax[0]] -= 1
			tmp = chr(imax[0] + 65) + " " + tmp
			
		result += tmp + " "
			
	return result

if __name__ == "__main__":
	T = int(input())
	for i in range(1, T + 1):
		print("Case #{}: {}".format(i, solve()))