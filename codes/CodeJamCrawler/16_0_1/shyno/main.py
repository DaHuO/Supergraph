'''
Counting Sheep
'''

if __name__ == '__main__':
    f = open("A-large.in")
    nc = int(f.readline())
    for x in xrange(1, nc+1):
        n = int(f.readline())
        result = 'INSOMNIA'
        if n:
            k = ''
            for i in xrange(1, 10 ** 10):
                k += str(n * i)
                if len(set(str(k))) == 10:
                    result = str(n * i)
                    break
        print "Case #%d: %s" % (x, result)
