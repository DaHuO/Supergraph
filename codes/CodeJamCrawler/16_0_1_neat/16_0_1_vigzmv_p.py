sums = []
fib_dict = {}
fibsum=[]

def powerset(s):
	x = len(s)
	d = []
	for i in range(1,1 << x):
		d = [s[j] for j in range(x) if (i & (1 << j))]
		fibsum.append(fib(sum(d)))

def fib(n):
    v1, v2, v3 = 1, 1, 0    # initialise a matrix [[1,1],[1,0]]
    for rec in bin(n)[3:]:  # perform fast exponentiation of the matrix (quickly raise it to the nth power)
        calc = v2*v2
        v1, v2, v3 = v1*v1+calc, (v1+v3)*v2, calc+v3*v3
        if rec=='1':    v1, v2, v3 = v1+v2, v1, v2
    return v2


n,m = map(int, raw_input().split())
a = map(int, raw_input().split())
for i in range(0,m):
	q = raw_input()
	if q[0] == 'Q':
		l = int(q[2])
		r = int(q[4])
		fibsum=[]
		qs = a[l-1:r]
		powerset(qs)
		print (sum(fibsum) % 1000000007)