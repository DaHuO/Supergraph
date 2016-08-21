from sys import argv
lines = open(argv[1]).readlines()
numcases = int(lines[0])




complete = set(range(10))
for i, n in enumerate(map(int, lines[1:])):
    if n==0:
        print 'Case #%d: INSOMNIA' % (i+1)
        continue
    mult = 1
    digits = set(map(int, [c for c in str(n)]))
    while n%10 == 0:
        digits.add(0)
        n/=10
        mult*=10
    oldn = n
    while digits!=complete:
        n+=oldn
        digits.update(map(int, [c for c in str(n)]))
    print 'Case #%d: %d' %(i+1, n*mult)
