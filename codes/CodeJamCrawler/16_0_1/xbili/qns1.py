import os, sys

def counting_sheep(n):
    if n == 0:
        return 'INSOMNIA'
    l = [None] * 10
    i = 1
    tmp = n
    while None in l:
        tmp = n * i
        for k in list(str(tmp)):
            l[int(k)] = True
        i += 1
    return tmp

if __name__ == '__main__':
    out = open(sys.argv[2], 'w')
    f = open(sys.argv[1])
    testcases = f.readline()

    for i in xrange(1, int(testcases)+1):
        n = f.readline()
        ans = counting_sheep(int(n))
        res = "Case #{i}: {ans}\n".format(i=i, ans=ans)

        out.write(res)
