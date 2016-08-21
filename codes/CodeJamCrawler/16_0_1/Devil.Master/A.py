def sheep(num):
    num_i=int(num)
    se=set(num)
    i=1
    if num_i==0:
        return 'INSOMNIA'
    while len(se)!= 10:
        num=num_i*i
        num=str(num)
        se|=set(num)
        #print num,se
        i+=1
    return num
for i in xrange(int(raw_input().strip())):
    print "Case #%d: %s" %(i+1,sheep(raw_input().strip()))
    # print "Case #%d: %s" % (i + 1, sheep(str(i)))