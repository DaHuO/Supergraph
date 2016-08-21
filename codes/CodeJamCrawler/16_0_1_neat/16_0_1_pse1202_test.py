filename = 'A-large.in'
f = open(filename,'r')

def g(n):
    a = set()
    k = 0
    while len(a)<10:
        k += 1
        for i in str(k*n):
            a.add(i)
    return k

T = int(f.readline())
for i in range(1,T+1):
	ans = ""
	n = int(f.readline())
	if n == 0:
		ans = "INSOMNIA"
	else:
		ans = str(n*g(n))
	print "Case #" + str(i) + ": " + ans
