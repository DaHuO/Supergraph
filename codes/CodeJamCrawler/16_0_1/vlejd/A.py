
def solve(t):
    N = input()
    print "Case #%d:"%(t+1),
    if N==0:
        print "INSOMNIA"
    else:
        seen = set()
        have = 0
        for i in xrange(1,100000):
            have+=N
            seen.update([x for x in str(have)])
            if len(seen)==10:
                print have
                break

def main():
    T = input()
    for i in xrange(T):
        solve(i)
    
if __name__=="__main__":
    main()