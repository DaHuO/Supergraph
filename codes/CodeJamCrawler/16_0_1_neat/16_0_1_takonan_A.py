import sys

def main(fin, fout):
	T = int(fin.readline())
	for t in range(T):
		N = int(fin.readline())
		seen = [0]*10
		print seen	
		answer = 0

		if N == 0:
			fout.write("Case #%d: INSOMNIA\n" % (t+1))
		else:
			# Get the digits
			N_str = str(N)
			for digit in N_str:
				seen[int(digit)] = 1
			
			curr_num = N
			while (sum(seen) < 10):
				curr_num += N 
				# Get the digits
				N_str = str(curr_num)
				for digit in N_str:
					seen[int(digit)] = 1
				if curr_num/(N+1) > 1000:
					break
				print seen
			
			if curr_num > 100000:
				answer = 0
			else:
				answer = curr_num

			if answer == 0:
				fout.write("Case #%d: INSOMNIA\n" % (t+1))
			else:
				fout.write("Case #%d: %d\n" % (t+1, answer))
	return

if __name__ == '__main__':
	fin = open(sys.argv[1], "r")
	fout = open(sys.argv[2], "w")
	main(fin, fout)
