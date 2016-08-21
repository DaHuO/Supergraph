import sys
import time

def min_flips(pstack):
	flips = 0
	for i in range(len(pstack)-2):
		if pstack[i] != pstack[i+1]:
			flips += 1
	if pstack[-2] == '-':
		flips += 1
	# print pstack, flips
	return flips

def main():
	start_time = time.time()
	input_file = sys.argv[1]
	with open(input_file, 'r') as f:
		lines = f.readlines()
	for i in range(1,len(lines)):
		print "Case #%d: %d" % (i, min_flips(lines[i]) )
	# print "Time (seconds):", time.time()-start_time


if __name__ == "__main__":
	main()