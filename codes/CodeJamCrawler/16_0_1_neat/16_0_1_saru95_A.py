import sys

i = 0 
n = 0
m = 0

def main():
	test_cases = int(raw_input())
	global n
	global i
	global m
	for case in xrange(test_cases):
		flag = 1
		tracker = dict()
		tracker[0] = 0
		tracker[1] = 0
		tracker[2] = 0
		tracker[3] = 0
		tracker[4] = 0
		tracker[5] = 0
		tracker[6] = 0
		tracker[7] = 0
		tracker[8] = 0
		tracker[9] = 0
		n = int(raw_input())
		i = 0
		while 0 in tracker.values():
			i += 1
			m = n * i
			#print i, m
			if i>1 and m==n:
				flag = 0
				break
			n_list = map(int, str(m))
			for j in xrange(len(n_list)):
				tracker[n_list[j]] += 1
		if flag == 0:
			print "Case #{}: {}".format(case+1, "INSOMNIA")
		else:
			print "Case #{}: {}".format(case+1, m)



if __name__ == '__main__':
	main()