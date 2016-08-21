from Queue import Queue

f = open("B-large.in", 'r')
ff = open("ans.txt", 'w')
n = int(f.readline())
for p in range(n):
    startStr = f.readline().strip()
    q = Queue()
    count = 0
    for symb in startStr:
        if q.empty():
            q.put(symb)
        else:
            popped = q.get()
            if popped != symb:
                count += 1
            q.put(symb)
    if q.get() == '-':
        count += 1
    ff.write("Case #%d: %d\n" % (p + 1, count))
ff.close()
f.close()
