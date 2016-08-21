from collections import deque
t = int(input())
for _ in range(t):
    s = list(input())
    q = deque([])
    for i in s:
        if len(q) == 0:
            q.append(i)
        else:
            if i >= q[0]:
                q.appendleft(i)
            else:
                q.append(i)
    print("Case #%d: %s" % (_+1, "".join(q)))
