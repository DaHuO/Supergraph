import sys

if len(sys.argv) > 1:
	filename = sys.argv[1]
else:
	filename = 'A-large.in'

# open the file for reading
f = open(filename, 'r')
T = int(f.readline())	# number of test cases

f_out = open('output.out', 'w')

for idx in range(1,T+1):
	digits_seen = set()
	N = int(f.readline())
	if N == 0:
		res = 'Case #{}: {}'.format(idx, 'INSOMNIA')
		f_out.write(res+'\n')
		print(res)
		continue

	i = -1
	while(len(digits_seen) < 10):
		i += 1
		N_str = str(N*(i+1))
		N_list = [int(x) for x in N_str]
		for y in N_list:
			digits_seen.add(y)
	res = 'Case #{}: {}'.format(idx, N*(i+1))
	f_out.write(res+'\n')
	print(res) 