INPUT_FILE = 'D-small-attempt0.in'
OUTPUT_FILE = 'D_out.txt'

with open(INPUT_FILE, 'r') as f:
	with open(OUTPUT_FILE, 'w') as f_out:
		T = int(f.readline().strip())
		for i in range(T):
			vars = f.readline().strip().split(' ')
			K = int(vars[0])
			C = int(vars[1])
			S = int(vars[2])
			# assuming K == S
			f_out.write('Case #'+str(i+1)+': ' + ' '.join(map(lambda x: str(x + 1), range(S))) + '\n')