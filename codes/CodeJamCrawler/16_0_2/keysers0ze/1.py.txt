
def count(str, c):
		
	sig = {"+" : True, "-" : False}
	
	chainsign = True if (str[0] == "+") else False
	cnt = 0
	
	for sign in str:
		if sig[sign] != chainsign:
			cnt += 1
			chainsign = not chainsign
	
	if chainsign == False:
		cnt += 1
	
	print "Case #%d: %d" % (c, cnt)
T = int(raw_input().strip())

for t in xrange(T):
	str = raw_input().strip()
	count(str, t+1)