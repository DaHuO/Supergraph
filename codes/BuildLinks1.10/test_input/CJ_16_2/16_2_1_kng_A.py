input_file = open('A-large.in', 'r+')
output_file = open('A-large.out', 'w+')
t = int(input_file.readline())
c = 0
while(c<t):
	c += 1
	s = input_file.readline().strip()
	A = [0 for _ in xrange(26)]
	for x in s:
		A[ord(x)-65] += 1
	n = []
	#Z-0
	if(A[25]>0):
		n += [0 for _ in xrange(A[25])]
		A[ord('E')-65] -= A[25]
		A[ord('R')-65] -= A[25]
		A[ord('O')-65] -= A[25]
		A[25] = 0
	#W-2
	if(A[22]>0):
		n += [2 for _ in xrange(A[22])]
		A[ord('T')-65] -= A[22]
		A[ord('O')-65] -= A[22]
		A[22] = 0
	#U-4
	if(A[20]>0):
		n += [4 for _ in xrange(A[20])]
		A[ord('F')-65] -= A[20]
		A[ord('O')-65] -= A[20]
		A[ord('R')-65] -= A[20]
		A[20] = 0
	#X-6
	if(A[23]>0):
		n += [6 for _ in xrange(A[23])]
		A[ord('S')-65] -= A[23]
		A[ord('I')-65] -= A[23]
		A[23] = 0
	#G-8
	if(A[6]>0):
		n += [8 for _ in xrange(A[6])]
		A[ord('E')-65] -= A[6]
		A[ord('I')-65] -= A[6]
		A[ord('H')-65] -= A[6]
		A[ord('T')-65] -= A[6]
		A[6] = 0
	#O-1
	if(A[14]>0):
		n += [1 for _ in xrange(A[14])]
		A[ord('E')-65] -= A[14]
		A[ord('N')-65] -= A[14]
		A[14] = 0
	#H-3
	if(A[7]>0):
		n += [3 for _ in xrange(A[7])]
		A[ord('T')-65] -= A[7]
		A[ord('R')-65] -= A[7]
		A[ord('E')-65] -= A[7]
		A[ord('E')-65] -= A[7]
		A[7] = 0
	#F-5
	if(A[5]>0):
		n += [5 for _ in xrange(A[5])]
		A[ord('I')-65] -= A[5]
		A[ord('V')-65] -= A[5]
		A[ord('E')-65] -= A[5]
		A[5] = 0
	#V-7
	if(A[21]>0):
		n += [7 for _ in xrange(A[21])]
		A[ord('S')-65] -= A[21]
		A[ord('N')-65] -= A[21]
		A[ord('E')-65] -= A[21]
		A[ord('E')-65] -= A[21]
		A[21] = 0
	#I-9
	if(A[8]>0):
		n += [9 for _ in xrange(A[8])]
	n.sort()
	o = ''
	for d in n:
		o += str(d)
	output_file.write('Case #'+str(c)+': '+str(o)+'\n')
