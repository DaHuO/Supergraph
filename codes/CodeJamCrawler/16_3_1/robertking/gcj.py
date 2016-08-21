import heapq
data = iter(open('A-large (2).in').read().splitlines())
cases = int(next(data))
abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for case in range(1, cases + 1):
    n = int(next(data))
    x = map(int, next(data).split())
    h = []
    for count, c in zip(x, abc):
        h.append((-count, c))
    heapq.heapify(h)
    solution = []
    while h:
        count, c = heapq.heappop(h)
        solution.append((c, count))
        count += 1
        if count < 0:
            heapq.heappush(h, (count, c))
    x1, x2 = solution.pop()[0], solution.pop()[0]
    solution = solution[::-1]
    ans = []
    while solution:
        c, count1 = solution.pop()
        if solution and solution[-1][1] == count1:
            c += solution.pop()[0]
        ans.append(c)
    ans.append(x1 + x2)
    print "Case #%d: %s" % (case, " ".join(ans))


