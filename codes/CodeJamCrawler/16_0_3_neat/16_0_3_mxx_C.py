
def is_jam(s): # if s is jam, return list of divisors, else return False
    div = []
    for b in xrange(2, 11):
        n = int(s, base=b)
        from math import sqrt; from itertools import count, islice
        for i in islice(count(2), int(sqrt(n)-1)):
            if i>1000000: return False
            if n%i==0: 
                div.append(i)
                break
        else: return False
    return div

if __name__=='__main__':
    print "Case #1:"
    N, J = 32, 500
    def k_to_str(k):
        reg = '{0:0%db}' % (N-2)
        return '1'+reg.format(k)+'1'
    k = 0
    while J>0:
        s = k_to_str(k)
        div = is_jam(s)
        while div==False: 
            k+=1
            s = k_to_str(k)
            div = is_jam(s)
        J -= 1
        k += 1
        print s,
        for d in div: print d,
        print ''
            
            
        

