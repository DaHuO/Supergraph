t = int(input())
s = set()
times = 0
for i in range(t):
    global s
    global times
    n = int(input())
    fill = True
    if(n==0):
        print("Case #"+str(i+1)+": "+"INSOMNIA")
        fill = False
    cur = n
    while(fill):
        times = times + 1
        s = s | set(str(cur))
        if(len(s)==10):
            fill = False
        else:
            cur = n * (times+1)
    if(n!=0):
        print("Case #"+str(i+1)+": "+str(cur))
    times = 0
    s = set()
