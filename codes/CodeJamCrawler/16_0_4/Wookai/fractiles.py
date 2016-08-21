import sys

def fractiles(K, C, S):
	if S < K:
		return 'IMPOSSIBLE'
		
	return ' '.join(map(str, range(1, K + 1)))

def main():
	T = int(sys.stdin.readline().strip())
	
	for i in range(T):
		K, C, S = map(int, sys.stdin.readline().strip().split())
		print("Case #{0}: {1}".format(i+1, fractiles(K, C, S)))
		
if __name__ == '__main__':
	main()