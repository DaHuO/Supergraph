MAX_ITER = 200

def sheep(n):
    left = {i for i in range(10)}
    not_changed = 0
    i = 0
    while not_changed < MAX_ITER and len(left) > 0:
        i+=1
        x = remove(left, i*n)
        if len(x) == 0:
            not_changed+=1
        else:
            #print "left=", left
            #print "x=", x
            not_changed = 0
            left.difference_update(x)

    if not_changed == MAX_ITER:
        return "INSOMNIA"

    #print "last number is", i*n
    #print "with", i, "iterations"
    return i*n


def remove(left, n):
    x = set()
    for i in str(n):
        i = int(i)
        if i in left and i not in x:
            x.add(i)
    return x


T = int(raw_input())
for i in range(T):
    x = sheep(int(raw_input()))
    print "Case #%s: %s" % (i+1,x)
