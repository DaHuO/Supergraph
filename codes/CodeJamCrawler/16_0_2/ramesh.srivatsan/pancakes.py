import numpy as np
import Queue
dict = {'+':1, '-':0}

def flip(s , n):
    s = np.array(list((1-s[:n])[::-1]) + list(s[n:]))
    return s

t = int(raw_input())
for i in range(t):
    s = np.array([dict[l] for l in str(raw_input())])
    n = len(s)
    vis=[]
    if [1]*n == list(s):
        print 'Case #'+str(i+1)+': 0'
        continue
    q = Queue.Queue()
    q.put((s,0))
    flag = 0
    vis.append(list(s))
    while q.not_empty:
        (s, d) = q.get()
        for j in range(n):
            a = flip(s, j+1)
            try:
                vis.index(list(a))
                continue
            except:
                if sum(a)==n:
                    print 'Case #'+str(i+1)+': '+str(d+1)
                    flag = 1
                    break
                q.put((a, d+1))
                vis.append(list(a))
        if flag == 1:
            break
