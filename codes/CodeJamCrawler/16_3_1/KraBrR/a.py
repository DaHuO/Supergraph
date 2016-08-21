#!/usr/bin/env python

ncase = int(raw_input())
for cidx in range(ncase):
    result = []
    nparties = int(raw_input())
    pstr = raw_input()
    pmembers = pstr.split()
    pmembers = [int(x) for x in pmembers]

    while not all(x == 0 for x in pmembers):
        tmp = list(pmembers)
        max_members_1 = max(tmp)
        index_1 = tmp.index(max_members_1)
        tmp.pop(index_1)
        max_members_2 = max(tmp)
        index_2 = tmp.index(max_members_2)
        if index_2 >= index_1:
            index_2 += 1

        if max_members_1 > max_members_2 + 2:
            index_2 = index_1

        group = ""
        last_three = False
        filtered = filter(lambda x: x == 1, pmembers)
        if sum(pmembers) == 3 and len(filtered) == 3:
            last_three = True

        pmembers[index_1] -= 1
        group += chr(index_1 + ord('A'))

        if last_three:
            result.append(group)
            continue

        if pmembers[index_2] > 0:
            pmembers[index_2] -= 1
            group += chr(index_2 + ord('A'))

        result.append(group)

    print "Case #{}: {}".format(cidx + 1, " ".join(result))
