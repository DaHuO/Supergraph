def main():
    f_inp = open('A-large.in')
    f_out = open('A-large.out', 'w')
    inp = f_inp.read().split('\n')
    inp = inp[:-1]
    inp = map(int, inp)
    n = inp[0]
    for j in range(1,n+1):
        m = inp[j]
        #m1 = m
        l = set(list(str(m)))
        i = 1
        m2 = 0
        #x = factors(m)
        #print x
        if(m == 0):
            f_out.write('Case #'+str(j)+': INSOMNIA\n')
        else:
            while(len(l)!=10):
                i += 1
                m2 = m*i
                l.update(list(str(m2)))
                #print l
            #if len(l) == 10:
            f_out.write('Case #'+str(j)+': '+str(m2)+'\n')
#def factors(n):
#    return set(reduce(list.__add__,
#                ([i] for i in range(1, 9) if n % i == 0)))

if __name__ == "__main__":
    main()
