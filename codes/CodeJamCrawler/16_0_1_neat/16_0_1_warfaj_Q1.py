





def seen_all(m):
    l = [0,1,2,3,4,5,6,7,8,9]
    seen = True
    for i in l:
        seen = seen and (i in m)
    return seen

def add_digits(n,m):
    while(n!= 0):
        x = n%10
        m[x] = True
        n /= 10
    return m



def last_seen(n):
    m = dict()
    x = n
    i = 2
    last = n
    seen = dict()
    while(not seen_all(m)):
        seen[x] = True
        m = add_digits(x,m)
        last = x
        x = i*n
        i += 1
        if x in seen:
            return None
    return last





t = int(raw_input())  # read a line with a single integer

answers = []

for i in xrange(1, t + 1):
  n = int(raw_input())
  answers.append(last_seen(n))

for i in xrange(t):
    a = answers[i]
    s = ""
    if a == None:
        s = "INSOMNIA"
    else:
        s = str(a)
    print "Case #"+str(i+1)+": "+s





