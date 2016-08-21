import sys
import random
import threading
import subprocess
sys.setrecursionlimit(10000)


def enumall(a, k):
    if k == 0:
        yield []
        return

    if len(a) < k:
        return

    for x in enumall(a[1:], k-1):
        yield [a[0]] + x
    for x in  enumall(a[1:], k):
        yield x


def calc2(x, y):
    res = 1
    for xx in x:
        res *= xx
    for yy in y:
        res *= 1-yy
#print x, y ,res
    return res


def sub(a, x):
    i = 0
    j = 0
    res = []
    while True:
        if j >= len(x):
            break
        if a[i] == x[j]:
            i += 1
            j += 1
        else:
            res.append(a[i])
            i += 1
    while i < len(a):
        res.append(a[i])
        i += 1
    return res

def calc(a):
    n = len(a)/2
    res = 0
    for x in enumall(a, n):
        y = sub(a, x)
        res += calc2(x, y)
    return res

def foo(line1, line2):
    n, k  = [int(x) for  x in line1.split()]
    a = [float(x) for x in line2.split()]
    a.sort()

    res = 0
    for x in enumall(a, k):
        res = max(res, calc(x))
    return '%f' % res


def main2():
    ifile = sys.stdin
    sys.stdout.write(foo(ifile.readline(), ifile.readline()))

#def main():
#    ifile = sys.stdin
#    n = int(ifile.readline())
#    for i in range(n):
#        print 'Case #%d: %s' % (i+1, foo(ifile))
#        sys.stdout.flush()

class MyT(threading.Thread):
    def __init__(self, line1, line2, res, idx):
        super(MyT, self).__init__()
        self.line1 = line1
        self.line2 = line2
        self.res = res
        self.idx = idx

    def run(self):
        p = subprocess.Popen(['python', '22.py', '2'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        p.stdin.write(self.line1)
        p.stdin.write(self.line2)
        p.wait()
        self.res[self.idx] = p.stdout.read()
        #print self.res

def main():
    ifile = sys.stdin
    n = int(ifile.readline())
    threads = [None]*n
    res = [None]*n
    for i in range(n):
        line1 = ifile.readline()
        line2 = ifile.readline()
        threads[i] = MyT(line1, line2, res, i)
        threads[i].start()
    for i in range(n):
        threads[i].join()
        print 'Case #%d: %s' % (i+1, res[i])
        sys.stdout.flush()

if len(sys.argv) == 1:
    main()
else:
    main2()

