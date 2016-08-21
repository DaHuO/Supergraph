
#t = int(raw_input())  # read a line with a single integer
#for i in xrange(1, t + 1):
#  n = int(raw_input())
#  print "Case #{}: {} ".format(i, last_num(n))

def last_num(n):
    if n == 0:
       return('INSOMNIA')
    digit_count = [0]*10
    for i in digits(n):
        digit_count[i] = digit_count[i] + 1
    sumn = n
    while 0 in digit_count:
        sumn = sumn + n
        for i in digits(sumn):
            digit_count[i] = digit_count[i] + 1
    return sumn

def digits(n) :
    l = [n % 10]
    n = n//10
    while n != 0:
        l.append(n%10)
        n = n//10
    return l


        
    
    
    




