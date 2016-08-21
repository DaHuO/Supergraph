# Problem 1: counting sheep
def count_sheep(num):
	if num==0:
		return 'INSOMNIA'
	else:
		i = 1
		seen = {}
		while len(seen.keys())<10:
			see = num * i
			digits = str(see)
			for digit in digits:
				if not seen.has_key(digit):
					seen[digit] = 1
			i = i + 1
		return see

f_output = open('A-large.out','w')
with open('A-large.in','r') as f:
	t = int(f.readline())
	for idx in xrange(1,t+1):
		num = int(f.readline())
		output= count_sheep(num)
  		f_output.writelines("Case #{}: {}\n".format(idx, output))
f_output.close()