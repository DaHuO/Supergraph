#author: prasunkgupta

N,J = 16,50
S='1'+14*'0'+'1'

def lowestfactor(n):
	if n%2 == 0:
		return 2
	i = 3
	while i <= (int(n**0.5) + 3):
		if n%i == 0:
			return i
		i+=2
	return n

outfile = open("C.out", "w")

for i in xrange(pow(2,(N-2))):
	S2 = int(S, 2)
	S3 = int(S, 3)
	S4 = int(S, 4)
	# print S4
	S5 = int(S, 5)
	S6 = int(S, 6)
	S7 = int(S, 7)
	S8 = int(S, 8)
	S9 = int(S, 9)
	S10 = int(S)
	# S = str(S10)
	S = str(bin(S2+2)[2:])

	fS2 = lowestfactor(S2)
	fS3 = lowestfactor(S3) 
	fS4 = lowestfactor(S4) 
	fS5 = lowestfactor(S5) 
	fS6 = lowestfactor(S6) 
	fS7 = lowestfactor(S7) 
	fS8 = lowestfactor(S8) 
	fS9 = lowestfactor(S9) 
	fS10 = lowestfactor(S10)

	if 	S2 ==fS2 or \
		S3 ==fS3 or \
		S4 ==fS4 or \
		S5 ==fS5 or \
		S6 ==fS6 or \
		S7 ==fS7 or \
		S8 ==fS8 or \
		S9 ==fS9 or \
		S10 ==fS10:
		continue
	else:
		outfile.write("%d %d %d %d %d %d %d %d %d %d"%(S10, fS2, fS3, fS4, fS5, fS6, fS7, fS8, fS9, fS10))
		print S10, fS2, fS3, fS4, fS5, fS6, fS7, fS8, fS9, fS10
		J = J-1
		if J == 0:
			break
	
outfile.close()
print "ok"