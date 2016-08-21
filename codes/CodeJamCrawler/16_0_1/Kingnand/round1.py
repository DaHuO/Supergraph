'''
Created on Apr 9, 2016

@author: kingnand
'''
def counting_sheep(ith, n):
    if n == 0:
        print 'Case #' + str(ith) + ': INSOMNIA'
        return
    m = {}
    multi=1
    while(len(m.keys()) < 10):
        num=n*multi
        detach_digit(num, m)
        multi+=1
    print 'Case #' + str(ith) + ': ' + str(n*(multi-1))
            
def detach_digit(n, m={}):
    while(n!=0):
        digit = n%10
        m[digit] = 1
        n=n/10
    return m


if __name__ == '__main__':
    with open('A-large.in', 'r') as f:
        num=0
        i=0
        for line in f:
            if i==0:
                num=int(line)
            else:
                counting_sheep(i, int(line))
            i+=1
           
                