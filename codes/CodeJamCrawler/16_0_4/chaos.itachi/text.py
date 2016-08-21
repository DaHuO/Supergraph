T = int(raw_input())
for _t in xrange(1,T+1):
	K,C,S = map(int,raw_input().split())
	aa = map(str,range(1,S+1))
	print "Case #" +str(_t)+":" , " ".join(aa)