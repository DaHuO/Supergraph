T = int(raw_input())
m = []
n = 0

def foo(N):
    global d
    for item in str(N):
        if int(item) not in d:
            d+=[int(item)]
def lol():
    i = 2
    global counter
    counter = 1
    while (sorted(d)!= m and counter < 100000000):
        foo(i*N)
        i = i+1
        counter += 1
    if (sorted(d)!= m and counter == 100000000):
        print "Case #%d: "%(n), "INSOMNIA"
    elif (sorted(d) == m):
        print "Case #%d: "%(n), ((i-1)*N) 

for item in range(0,10):
    m += [item]
while(T>0):
    global n
    n += 1
    global d
    d = []
    N = int(raw_input())
    foo(N)
    lol()
    T-=1





