def solve(s):
	out = [];
	s = list(s)
	while(len(s) != 0):
		#print(s)

		if('Z' in s):
			for j in nums[0]:
				s.remove(j)
			out.append(0)
		elif('W' in s):
			for j in nums[2]:
				s.remove(j)
			out.append(2)

		elif('U' in s):
			for j in nums[4]:
				s.remove(j)
			out.append(4)

		elif('F' in s):
			for j in nums[5]:
				s.remove(j)
			out.append(5)

		elif('X' in s):
			for j in nums[6]:
				s.remove(j)
			out.append(6)
		elif('V' in s):
			for j in nums[7]:
				s.remove(j)
			out.append(7)
		elif('G' in s):
			for j in nums[8]:
				s.remove(j)
			out.append(8)
		elif('O' in s):
			for j in nums[1]:
				s.remove(j)
			out.append(1)
		elif('H' in s):
			for j in nums[3]:
				s.remove(j)
			out.append(3)
		elif('I' in s):
			for j in nums[9]:
				s.remove(j)
			out.append(9)
	out = sorted(out)
	outstr=''
	for i in out:
		outstr+= ''+str(i)
	return outstr

out = ''
f = open("A-large.in",'r')
# f = open("in.txt",'r')
o = open("outfile.txt",'w')
i = eval(f.readline())

nums = ['ZERO','ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE']

stack = 'OZONETOWER'
for n in range(i):
	s = f.readline()
	if(s[-1:] == '\n'):
		s = s[:-1]
	# print(solve('s'))


	out += 'Case #' +str(n+1) +': '+str(solve(s))+'\n'


o.write(out[:-1])


o.close()
f.close()