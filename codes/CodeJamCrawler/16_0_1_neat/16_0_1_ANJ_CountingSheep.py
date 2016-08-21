T = input()


def getDigits(n):
    s = list(str(n))
    st = set()
    for c in s:
        st.add(int(c))
    return st


def counting(n):
    if n==0:
        return n
    s = getDigits(n)
    ln = len(s)
    i = 2
    num = n
    while ln < 10:
        num = i*n
        s1 = getDigits(num)
        s = s | s1
        ln = len(s)
        i += 1
    return num


for i in xrange(1, T+1):
    n = input()
    res = counting(n)
    if res > 0:
        print "case #" + str(i) + ": " + str(res)
    else:
        print "case #" + str(i) + ": INSOMNIA"
