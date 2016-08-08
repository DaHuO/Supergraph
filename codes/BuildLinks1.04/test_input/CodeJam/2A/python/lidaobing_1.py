import sys
import numpy
sys.setrecursionlimit(10000)


b = [
"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"
]

c = [[0]*26 for i in range(10)]
for i in range(10):
	for x in b[i]:
		c[i][ord(x)-ord('A')] += 1

allletters = sorted(''.join(list(set(list(sorted(''.join(b)))))))
tenletters = allletters[:10]


d = [[0]*10 for i in range(10)]
for i in range(10):
	for j in range(10):
		d[j][i] = b[i].count(tenletters[j])


foo2 = {}
foo2['RS'] = 'R'
foo2['SR'] = 'R'
foo2['SP'] = 'S'
foo2['PS'] = 'S'
foo2['PR'] = 'P'
foo2['RP'] = 'P'



def check(a):
	if len(a) == 1:
		return True
	res = ''
	for i in range(0, len(a), 2):
		if a[i] == a[i+1]:
			return False
		res += foo2[a[i:i+2]]
	return check(res)


a = [None]*13

def main2():
	a[0] = [0, 0, 1]
	for i in range(1, 13):
		t1 = a[i-1][:]
		t2 = t1[::-1]
		t3 = [0]*3
		t3[0] = t1[0]+t2[0]
		t3[1] = t1[1]+t2[1]
		t3[2] = t1[2] + t2[2]
		t3.sort()
		a[i] = t3

def vecadd(b, c):
	return [b[0]+c[0],
	b[1]+c[1],
	b[2]+c[2]]

def split(n, res):
	a1 = a[n-1]
	a2 = a1[1:] + [a1[0]]
	a3 = a2[1:]+ [a2[0]]
	if vecadd(a1,a2) == res:
		return a1, a2
	if vecadd(a1,a3) == res:
		return a1, a3
	if vecadd(a2,a3) == res:
		return a2, a3
	print 'ERROR'

def foo3(res):
	#print res
	res = list(res)
	level = 1
	while level+level <= len(res): 
		for i in range(0, len(res), 2*level):
			if res[i:i+level] > res[i+level:i+level+level]:
				res[i:i+level], res[i+level:i+level+level] = res[i+level:i+level+level], res[i:i+level]
		level*=2
	return ''.join(res)


def foo2(n, aa):
	if n == 1:
		res = ''
		if aa[0] > 0:
			res += 'R'
		if aa[1] > 0:
			res += 'P'
		if aa[2] > 0:
			res += 'S'
		return res
	a1, a2 = split(n, aa)
	return foo2(n-1, a1)+foo2(n-1, a2)

	 




def foo(ifile):
	n, r, p, s = [int(x) for x in ifile.readline().split()]
	t = [r, p, s]
	t.sort()
	if t != a[n]:
		return 'IMPOSSIBLE'
	res = foo2(n, [r, p, s])
	return foo3(res)

 


def main():
    ifile = sys.stdin
    n = int(ifile.readline())
    for i in range(n):
        print 'Case #%d: %s' % (i+1, foo(ifile))

main2()
main()

