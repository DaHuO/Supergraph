#Rayun Mehrab - Qualification Problem A Large

t = int(raw_input())
    
def check_sleep():
    for i in xrange(0, 10):
        if l[i] == 0:
            return False
    return True

def set_l(n):
    while n>=10:
        a = n%10
        n = int(n/10)
        if l[a] == 0:
            l[a] = 1

    if l[n] == 0:
        l[n] = 1

    return

for i in xrange(1, t + 1):
    n = int(raw_input())
    l = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    b = 0

    if n == 0:
        print "Case #{}: INSOMNIA".format(i)
    else:
        while not check_sleep():
            b = b + n
            set_l(b)
            
        print "Case #{}: {}".format(i, b)

exit()
