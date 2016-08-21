
def find_number(seed):
    founds = []
    i=0
    if seed == 0:
            return 'INSOMNIA'

    while len(founds) < 10:
        i+=1
        for j in str(seed*i):
            if j not in founds:
                founds.append(j)

    return str(seed*i)

T=int(raw_input())
for i in xrange(T):
    print ("Case #%d: "%(i+1)+ find_number( int(raw_input())))