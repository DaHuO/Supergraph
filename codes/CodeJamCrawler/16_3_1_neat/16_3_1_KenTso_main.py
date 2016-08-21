#!/usr/bin/env python
from operator import itemgetter

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    no_parties = int(raw_input())
    party_people = [int(x) for x in raw_input().split()]
    no_people = sum(party_people)
    party_people = [[chr(ord('A') + x), y] for x, y in enumerate(party_people)]
    party_people = sorted(party_people, key=itemgetter(1, 0))

    evacuation_order = []
    while no_people > 0:
        if len(party_people) > 1:
            party1 = party_people[0]
            party2 = party_people[1]
            evacuation_order.append(party1[0] + party2[0])
            party1[1] -= 1
            party2[1] -= 1
            if party1[1] == 0 and party2[1] == 0:
                party_people = party_people[2:]
            elif party1[1] == 0:
                party_people = party_people[1:]
            no_people -= 2
        else:
            party = party_people[0]
            if party[1] == 1:
                evacuation_order.append(party[0])
                party_people = []
                no_people -= 1
            else:
                evacuation_order.append((party[0] * 2))
                party[1] -= 2
                no_people -= 2
    print "Case #{}: {}".format(i, " ".join(evacuation_order[::-1]))
