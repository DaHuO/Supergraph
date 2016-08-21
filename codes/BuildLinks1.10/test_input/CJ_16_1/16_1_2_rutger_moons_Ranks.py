__author__ = 'rutger'

problemName = "ranks.txt"
f = open(problemName, 'w')

def prettyArray(l):
    s = ""
    for c in l:
        s += " " + str(c)
    return s


def solve(lists):
    dict = {}
    for l in lists:
        for el in l:
            a = dict.get(el, -1)
            if a == -1:
                dict[el] = 1
            else:
                dict[el] = a + 1

    result = []
    for el in dict.items():
        if el[1] % 2 == 1:
            result.append(el[0])

    return sorted(result)


T = int(input())
for t in range(T):
    pass
    # do input
    n = int(input())

    lists = []
    for i in range(2*n - 1):
        l = list(map(int, input().split()))
        lists.append(l)

    # solve input
    result = solve(lists)

    # print result
    f.write("Case #%d:%s\n" % (t+1, prettyArray(result)))



f.close()