#Code Jam problem "Counting Sheep" Qualification Round 2016
#https://code.google.com/codejam/contest/6254486/dashboard
#-Thomas Steinke codejam@thomas-steinke.net 2016-04-08
import sys

#This function either solve the problem or doesn't halt.
def solve_sheep(N):
	assert type(N) == int
	assert 0 <= N
	if N==0: return "INSOMNIA"
	M=N
	appears = [0]*10
	while True:
		#print M #debug
		appearances=0
		for i in range(10):
			if str(i) in str(M): appears[i] = 1
			appearances = appearances + appears[i]
		#print appears #debug
		#print "Total seen so far = " + str(appearances) #debug
		if appearances == 10: return str(M)
		M=M+N

#build lookup table
def lookup_table(maxN):
	table = [""] * (maxN+1)
	for N in range(maxN+1):
		M=solve_sheep(N)
		#print str(N) + ": " + str(M) #debug
		table[N]=M
	return table

#solve instance
def main():
	T=int(sys.stdin.readline())
	for t in range(T):
		N=int(sys.stdin.readline())
		M=solve_sheep(N)
		print "Case #" + str(t+1) + ": " + M

######
main()

