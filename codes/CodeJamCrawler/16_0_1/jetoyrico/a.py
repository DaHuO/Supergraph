INPUT_FILE_NAME = 'A-large.in'
OUTPUT_FILE_NAME = 'out'

fin = open(INPUT_FILE_NAME)
fout = open(OUTPUT_FILE_NAME, 'w')

def f(n):
    if n == 0: return 'INSOMNIA'
    add = n
    a = [False] * 10
    while True:
        for c in str(n):
            a[int(c)] = True
        if ok(a):
            break
        n += add
    return n

def ok(a):
    for v in a:
        if not v:
            return False
    return True

for case in xrange(1, 1 + int(fin.readline())):
    n = int(fin.readline())
    fout.write("Case #%d: %s\n" % (case, str(f(n))))

fout.close()
fin.close()
