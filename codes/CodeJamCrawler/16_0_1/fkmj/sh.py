
def count(n):
    found = [False] * 10

    found_count = 0
    i = 0
    num = 0
    while found_count != 10:
        i += 1
        num += n
        nstr = str(num)
        for ch in nstr:
            idx = ord(ch) - ord('0')
            if not found[idx]:
                found_count += 1
                found[idx] = True
    return i*n

def work(c):
    n = int(raw_input())
    if n==0:
        print "Case #%d: INSOMNIA" % c
    else:
        print "Case #%d: %d" % (c, count(n))

def main():
    t = int(raw_input())
    for i in range(t):
        work(i+1)

def main2():
    for i in range(1,200):
        print i, count(i)/i
        
main()
