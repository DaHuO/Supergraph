def readint(): return int(raw_input())
def readarray(f): return map(f, raw_input().split())

T = readint()

def solve(string):
	if string[len(string)-1] == '-':
		val = 1
	else :
		val =0
	c = string[0]
	for i in range(1,len(string)):
		if c != string[i]:
			val = val + 1
			c = string[i]
	return val			

for t in range(T):
	N = raw_input()
	print 'Case #%i:'%(t+1), solve(N)
	
	
