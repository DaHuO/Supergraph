fi = open('small.in')
fi = open('A-large.in')
# fi = open('A-small-attempt0.in')
fo = open('aresult.out', 'w')

T = int(fi.readline())

occurrences = lambda s, lst: (i for i,e in enumerate(lst) if e == s)

def evacuate_senates(senates):
    parties = senates.keys()
    no_senates = senates.values()

    plan = list()
    while (parties):
        # print parties
        # print senates

        max_senates = max(no_senates)
        count = no_senates.count(max_senates)

        if count == 1:
            # remove 2 at the same time
            if max_senates >= 2:
                index = no_senates.index(max_senates)
                key = parties[index]
                senates[key] -= 2
                plan.append('%s%s' % (key, key))
            else:
                print no_senates
        elif count != 3:
            indices = list(occurrences(max_senates, no_senates))

            # remove senates for first two parties
            plan.append('%s%s' % (parties[indices[0]], parties[indices[1]]))
            senates[parties[indices[0]]] -= 1
            senates[parties[indices[1]]] -= 1
        else:
            index = no_senates.index(max_senates)
            key = parties[index]
            senates[key] -= 1
            plan.append('%s' % key)

        # Check if there is any parties with senates = 0
        parties = senates.keys()
        no_senates = senates.values()
        indices = list(occurrences(0, no_senates))
        for i in indices:
            senates.pop(parties[i])

        parties = senates.keys()
        no_senates = senates.values()

    return plan

for t in range(1, T+1):
    no_parties = int(fi.readline())
    no_senates = [int(x) for x in fi.readline().split(' ')]

    senates = dict()

    A_ascii_code = 65
    for i, senate in enumerate(no_senates):
        senates[str(unichr(i + A_ascii_code))] = senate

    plan = evacuate_senates(senates)

    output_val = ' '.join(plan)
    fo.write('Case #%i: %s\n' % (t, output_val))
