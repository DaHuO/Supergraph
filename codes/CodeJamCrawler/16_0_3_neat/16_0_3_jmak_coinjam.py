from itertools import product

outfile = open('coinjam_results.txt', 'w')
outfile.write('Case #' + str(1) + ':\n')

all_nums = ['1' + ''.join(seq) + '1' for seq in product("01", repeat=14)]

def get_factor(n):
    if not n & 1: 
        return 2
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return x
    return 0

counter = 0

for n in all_nums:
	if counter == 50:
		break
	cur_result = n
	for i in range(2, 11):
		f = get_factor(int(n, i))
		if f != 0:
			cur_result += ' ' + str(f)
		else:
			cur_result = None
			break
	if cur_result == None: continue
	outfile.write(cur_result + '\n')
	counter += 1

outfile.close()