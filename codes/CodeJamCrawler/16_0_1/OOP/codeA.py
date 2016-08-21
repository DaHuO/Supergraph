import itertools
def f(x):
    if not x:return "INSOMNIA"
    s=set()
    for i in itertools.count(x,x):
        s.update(str(i))
        if len(s)==10:return str(i)
for t in range(int(input())):
    print("Case #%d: %s"%(t+1,f(int(input()))))
