##from bisect import bisect
##for _ in range(int(raw_input())):
##    n = int(raw_input())
##    a = map(int, raw_input().split())
##	aa = a[::-1]
##	b = map(int, raw_input().split())
##	bb = b[::-1]
##	c = []
##	for i in range(n):
##		x = bisect(aa, bb[i])
##		if x > 0:
##			c.append(x - i-1)
##	print _, c		
##	if len(c):
##		print max(c)
##	else:
##		print 0          

##n = int(raw_input())
##a = int(raw_input())
##b = int(raw_input())
##c = int(raw_input())
##p = n / a
##g = 0
##while n >= b:
##    t = n / b
##    g += t
##    n -= t * b
##    n += t * c
##g += n / a    
##print max(p, g)

def filtest(n):
    t = map(int, str(n))
    for i in t:
        tst[i] = 1
    if tst == TTT:
        return True
    return False
        
TTT = 10 * [1]        
for t in range(int(raw_input())):
    tst = 10 * [0]
    n = int(raw_input())
    if n == 0:
        print "Case #%d: INSOMNIA"%(t+1)
    else:
        i = 1
        while not filtest(n*i):
            i += 1
        print "Case #%d: %d"%(t+1, n*i)    
            
            
        
        
    
