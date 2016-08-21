def Solution(i,num,layer,tag):
    if layer*tag < num:
        print "Case #{}: {}".format(i, 'IMPOSSIBLE')
        return
    res = []
    cnt = 0
    while cnt < num:
        fac = 0
        idx = 0
        for x in xrange(cnt+1, min(cnt+1+layer, num+1)):
            idx += (x-1)*(num**fac)
            #print x, num, fac, x*(num**fac)
            idx+=1 if fac==0 else 0
            fac+=1
        cnt+=layer
        res.append(idx)
        #print res
    res.sort()
    print "Case #{}: {}".format(i, " ".join(map(str,res)))
    return



if __name__ == '__main__':
    import sys

    file_name = sys.argv[1]
    with open(file_name) as f:
        line = f.readline()
        for i in xrange(1, int(line)+1):
            line = f.readline().strip('\n')
            K,C,S = line.split(' ')
            Solution(i, int(K), int(C), int(S))