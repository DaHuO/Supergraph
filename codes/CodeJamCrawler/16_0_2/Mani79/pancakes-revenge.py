from sys import stdin

def flip(list, i):
    l = list[0:i]
    for j in range(i):
        list[j] = 0 if l[i-j-1]==1 else 1

n = int(stdin.readline())

for i in range(n):
    L = [(0 if x=="-" else 1) for x in stdin.readline()]
    sz = len(L)-1  #extra newline character in the end
    ops = 0
    while True:
        while sz>0 and L[sz-1]==1:
            sz = sz-1
        if sz==0:
            break
        prefix = 0
        while prefix < sz-1 and L[prefix]==1:
            prefix = prefix+1
        if prefix >0:
            flip(L,prefix)
            ops = ops+1
        flip(L,sz)
        ops = ops+1
    print('Case #' + str(i+1) + ": " + str(ops))        

