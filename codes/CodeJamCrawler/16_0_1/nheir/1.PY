t = {0,1,2,3,4,5,6,7,8,9}

def f(n):
    m = n
    s = set( map(int,str(n)) )
    while s != t:
        n += m
        s |= set( map(int,str(n)) )
    return n

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        if n == 0:
            print('Case #%d: %s' % (i+1,'INSOMNIA'))
        else:
            print('Case #%d: %d' % (i+1,f(n)))