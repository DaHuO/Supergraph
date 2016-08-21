from collections import Counter

test = int(raw_input())
offset = ord('A')

for test_case in xrange(test):
    N = int(raw_input())
    senators = Counter()
    line = raw_input().split()
    for i in xrange(N):
        senators[chr(i + offset)] = int(line[i])

    ans = []
    if len(senators) == 2:
        elements = senators.most_common(2)
        p1, v1 = elements[0]
        p2, v2 = elements[1]
        ans += [p1 + p2] * v1
    else:
        total = sum(senators.values())
        biggest = max(senators.values())

        while total > 2*biggest:
            party, votes = senators.most_common()[:-2:-1][0]
            ans.extend(party)
            senators[party] -= 1
            total -= 1
            if senators[party] == 0:
                del senators[party]

        while any(senators):
            p1, votes1 = senators.most_common(1)[0]
            p2, votes2 = senators.most_common()[:-2:-1][0]
            ans += [p1 + p2] * votes2
            senators[p1] -= votes2
            del senators[p2]
            if senators[p1] == 0:
                del senators[p1]

    print "Case #{}: {}".format(test_case+1, " ".join(ans))