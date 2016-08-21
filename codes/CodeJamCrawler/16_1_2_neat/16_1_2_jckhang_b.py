import collections

t = int(raw_input())
# t round of input
for i in xrange(1, t + 1):
    # n rows
    n = int(raw_input())
    ls = []
    for j in xrange(1, 2 * n):
        row = raw_input()
        arr = row.split(" ")
        ls.append(arr)
    lls = reduce(lambda x, y: x + y, ls)
    counter = collections.Counter(lls)
    result = []
    for key, value in counter.iteritems():
        if int(value) % 2 == 1:
            result.append(int(key))
    result = sorted(result)
    print("Case #{}: {}".format(i, str(result)[1:-1]).replace(',', ''))
