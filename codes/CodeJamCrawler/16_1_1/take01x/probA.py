file = open("./A-large.in")
limit = int(file.readline())
index = 1
while limit > 0:
    S = list(file.readline())
    S.remove("\n")
    ans = []
    for i in xrange(len(S)):
        if i == 0 or ans[0] > S[i]:
            ans.append(S[i])
        else:
            ans.insert(0, S[i])
    print("Case #%d: %s" % (index, "".join(ans)))
    limit -= 1
    index += 1
