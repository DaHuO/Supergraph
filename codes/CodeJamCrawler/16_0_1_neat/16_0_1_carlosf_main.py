

if __name__=="__main__":
    T = input()
    for t in xrange(1, T+1):
        N = input()
        target = set(("0","1","2","3","4","5","6","7","8","9"))
        ntarget = 10
        i = 1
        if (N == 0):
            print("Case #%d: %s" % (t, "INSOMNIA"))
        else:
            while(ntarget > 0):
                numb = i*N
                for n in str(numb):
                    if (n in target):
                        target.remove(n)
                        ntarget -= 1
                i+=1
            
            print("Case #%d: %d" % (t, numb))

