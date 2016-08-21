t = int(input().strip())
for at in range(t):
    n = int(input().strip())

    p = list(map(int, input().strip().split(" ")))
    plan = []
    # dic = [0 for x in range(maj + 1)]
    while sum(p) != 0:
        first = max(p)
        eject = ''
        party = p.index(first)
        eject += chr(party + 65)
        p[party] -= 1
        second = max(p)  # new maj
        party = p.index(second)
        eject += chr(party + 65)
        p[party] -= 1
        if max(p) > sum(p)/2:
            eject = "".join(eject[:-1])
            p[party] += 1
        plan.append(eject)

    print('Case #{0}: {1}'.format(at+1, " ".join(plan)))
