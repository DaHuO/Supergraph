import math
import sys
import time

def last_number(N):
	if N == 0: return "INSOMNIA"
	digits = set(range(10))
	i = 1
	while len(digits) > 0:
		curNumber = i*N
		while curNumber >= 1:
			if curNumber%10 in digits:
				digits.remove(curNumber%10)
			curNumber /= 10
		i += 1
		if i > 100: return "INSOMNIA"
	return (i-1)*N

def main():
	start_time = time.time()
	input_file = sys.argv[1]
	with open(input_file, 'r') as f:
		lines = f.readlines()
	for i in range(1,len(lines)):
		print "Case #%d: " % i + str(last_number(int(lines[i])))
	# print "Time (seconds):", time.time()-start_time


if __name__ == "__main__":
	main()