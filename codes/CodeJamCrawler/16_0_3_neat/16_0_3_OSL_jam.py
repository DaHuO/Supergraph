import math 

n = 32
j = 500

b = [0] * n
b[n-2] = 1

def next(a):
	carry = 0;
	for i in range(n):
		a[n-i-1] += carry + b[n-i-1];
		carry = a[n-i-1] >= 2;
		if (carry):
			a[n-i-1] -= 2;
	return a

def toI(n, i):
	res = 0
	base = 1
	l = len(n)
	#print "transfering "
	for k in range(l):
		#print("iter, ", k)
		res += n[l-k-1] * base
		base *= i
	return res

def DDiv(a, bb):
	carry = 0
	cur = 0
	for i in range(len(a)):
		cur = int(a[i]) + carry * 10
		#a[i] = int (cur / b);
		carry = int (cur % bb);
	return carry

def isPrime(n):
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3

    i = 5
    w = 2
    ss = str(n)
    #print n
    while i * i <= n:
    	#print("iter, ", i)
        if n % i == 0:
            return i

        i += w
        w = 6 - w
        if i > 10**5:
        	return 0
    return 0

# def isPrime(n):
# 	ss = str(n)
# 	for i in range(2, int(math.sqrt(n)) +1 ):
# 		print("iter, ", i)
# 		if DDiv(ss, i) == 0:
# 			return i
# 	return 0
			
def check(n):
	# n == str 01101010
	res = []
	for i in range(2, 11):
		t = toI(n, i)
		#print(" to 1", t)
		r = isPrime(t)
		if r == 0:
			return False, 0
		else:
			res += [r]
			#print(n, " to ", i, " is ", t, " divisor is ", r)
	return True, res

def toStr(l, space=" "):
	return space.join(str(x) for x in l)

ans = []
div = {}
cnt = 0

s = [0] * n
s[0] = 1
s[n-1] = 1

while(cnt < j):
	print s
	r, t = check(s)
	if r==True:
		ss = toStr(s,"")
		ans += [ss]
		div[ss] = t
		cnt += 1
		print(cnt, "+1")

	s = next(s)

print("Case #1:")
for i in range(j):
	ress = toStr(div[ans[i]])
	print(ans[i] + " " +  ress)