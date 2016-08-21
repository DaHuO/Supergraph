from collections import defaultdict
from collections import OrderedDict
with open("testbig.in") as infile:
	ntests = int(infile.readline().rstrip())
	print ntests
	outfile = open("OutputRanklast.txt", 'w')
	for case in range(ntests):
		N = int(infile.readline())
		rows = []
		for line_num in range(2*N-1):
			row = [int(item) for item in infile.readline().rstrip().split(" ") if item != '']
			rows.append(row)
		hashmap = defaultdict(int)
		for row in rows:
			for item in row:
				hashmap[item] += 1
		# corted_keys = sorted(hashmap.keys())
		ordered_map  = OrderedDict(sorted(hashmap.items()))
		sorted_keys = ordered_map.keys()
		# middle = len(sorted_keys)/2 - 1
		middle = 0
		missing = []
		for i in range(len(sorted_keys)):
			key = sorted_keys[i]
			if hashmap[key]%2 != 0:
				missing.append(str(key))
		if len(missing) != N:
			missing.insert(0,str(N))
		ans = ' '.join(missing)
		print ans
		outfile.write("Case #{}: {} \n".format( case + 1, ans))




	

