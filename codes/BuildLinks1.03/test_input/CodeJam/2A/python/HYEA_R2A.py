
#"R" -> "SR"
#"S" -> "PS"
#"P" -> "RP"
	
RR = ["R"]
SS = ["S"]
PP = ["P"]
for i in range(12):
	sx=""
	px=""
	rx=""
	if SS[i]<PP[i]: sx = SS[i]+PP[i]
	else: sx = PP[i]+SS[i]
	if RR[i]<SS[i]: rx = RR[i]+SS[i]
	else: rx = SS[i]+RR[i]
	if PP[i]<RR[i]: px = PP[i]+RR[i]
	else: px = RR[i]+PP[i]
	RR.append(rx)
	SS.append(sx)
	PP.append(px)
	
#print RR[2]
	
def check(a, r, p, s):
	return (a.count("R") is r and a.count("P") is p and a.count("S") is s)
T=input()
for i in range(1, T+1):
	a, r, p, s = map(int,raw_input().split())
	
	ans = "IMPOSSIBLE"
	if check(RR[a],r,p,s): ans = RR[a]
	if check(SS[a],r,p,s): ans = SS[a]
	if check(PP[a],r,p,s): ans = PP[a]
	
	print "Case #%d: %s"%(i, ans)
	
	