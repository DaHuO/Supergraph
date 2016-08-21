__author__ = 'vitaly'

def f(n):
    if n == 0:
        return "INSOMNIA"
    s = set()
    m = 1
    while True:
        v = n * m
        for c in str(v):
            s.add(c)
        if len(s) == 10:
            return v
        m += 1
    return "INSOMNIA"


#res = open("res.txt", "w")
#inp = open("inp.txt", "r")
t = int(raw_input())
#t = int(inp.readline())
for i in range(t):
    #n = int(inp.readline())
    n = int(raw_input())
    #res.write("Case #{}: {}\n".format(i + 1, f(n)))
    print ("Case #{}: {}\n".format(i + 1, f(n)))