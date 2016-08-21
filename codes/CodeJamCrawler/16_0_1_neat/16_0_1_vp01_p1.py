test=input()


for i in xrange(test):

    num = raw_input()
    if num == '0':
        print 'Case #%d: INSOMNIA'%(i+1)
    else:

        number_str = num.rstrip('0')
        s = set(num)
        noz = len(num)-len(number_str)
        #multiplier = 2
        number = int(number_str)
        result = number
        
        while len(s)< 10:
            result +=number
            #print result,s,set(str(result))
            s=s.union(set(str(result)))
            #print s
            #raw_input()
        print 'Case #%d: %s'%(i+1,str(result)+('0'*noz))
            
        
