
def calc(k,c,s):
    if k < s:
        return "IMPOSSIBLE"
    else:
        li = []
        for i in range(k):
            li.append(str(i+1))
        return " ".join(li)
    

for case in range(input()):
    k, c, s = map(int,raw_input().strip().split())
    print "Case #"+str((case+1))+": "+str(calc(k,c,s))