H = '+'

def flip(s):
    # give me index
    cur = len(s) - 1
    # total count
    cnt = 0

    while(cur>=0):
        if s[cur]==H:
            cnt += 0
            cur = cur - 1
        else:
            while(cur>=0):
                if cur==0:
                    cnt += 1
                    cur = cur - 1
                else:
                    if s[cur-1]==H:
                        cnt += 2
                        cur = cur - 1
                        break
                    else:
                        cur = cur - 1
    
    return cnt


def dbg(msg):
    print msg
    pass

def main():
    t = int(raw_input())
    for i in xrange(1, t + 1):
        s = raw_input()
        n = flip(s)
        print "Case #{}: {}".format(i, n)

if __name__=='__main__':
    main()
