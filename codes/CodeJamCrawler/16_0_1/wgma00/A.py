import sys
sys.stdin = open("A-small-attempt0.in")

def update(n, v):
   '''populates the value of v with the digits in n '''
   while(n > 0):
       v[n%10] = True
       n //= 10

def done(v):
    ''' checks if all the elements are done in v'''
    for i in range(10):
        if(v[i] == False):
            return False
    return True

T = int(input())
for t in range(1, T+1):
    N = int(input())
    if(N == 0):
        print('Case #%d: INSOMNIA' % t)
    else:
        v = [False for i in range(10)]
        update(N, v)
        i = 1
        while(not done(v)):
            update(N*i, v)
            if(not done(v)):
                i += 1
        print('Case #%d: %d' %(t, N*i))


