T = int(raw_input())

def get_last(n):
    digits = [str(d) for d in range(10)]
    rm = []

    num = 0
    
    while (len(digits) > 0):
        num += n
        for d in digits:
            if d in str(num):
                rm.append(d)
        for d in rm:
            digits.remove(d)
        rm = []
        
    return num

for i in range(0, T):
    N = int(raw_input())
    if (N == 0):
        print 'Case #{0}: INSOMNIA'.format(i+1)

    else:
        print 'Case #{0}: {1}'.format(i+1, get_last(N))
