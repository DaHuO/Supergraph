import sys

def count_sheep(N):
	if N == 0:
		return 'INSOMNIA'
	
	digits = set()
	i = 1
	
	while True:
		digits = set(str(N * i)).union(digits)
		if len(digits) == 10:
			return i * N
		i += 1

def main():
	T = int(sys.stdin.readline().strip())
	
	for i in range(T):
		N = int(sys.stdin.readline().strip())
		print("Case #{0}: {1}".format(i+1, count_sheep(N)))
		
if __name__ == '__main__':
	main()