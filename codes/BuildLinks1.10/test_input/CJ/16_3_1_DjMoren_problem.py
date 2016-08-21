'''
Created on Apr 16, 2016

@author: hduser
'''
from string import ascii_uppercase


def solve(parties, senators):
    abecedary = list(ascii_uppercase)
    sol = list()
    while any(senators):
        max_value = max(senators)
        max_index = senators.index(max_value)
        if max_value % 2 == 0:
            senators[max_index] -= 1
            sol.append(abecedary[max_index])
            max_value = max(senators)
            max_index = senators.index(max_value)
            repeated_values = list([x for x in senators if x == max_value])
            if len(repeated_values) == 1:
                senators[max_index] -= 1
                sol[len(sol) - 1] += abecedary[max_index]
            else:
                indexes = [i for i, x in enumerate(senators) if x == max_value]
                index = indexes[0]
                if indexes[0] == max_index:
                    index = indexes[1]
                senators[index] -= 1
                sol[len(sol) - 1] += abecedary[index]
        else:
            senators[max_index] -= 1
            sol.append(abecedary[max_index])
            if any(senators):
                if sum(senators) != 2:
                    max_value = max(senators)
                    max_index = senators.index(max_value)
                    senators[max_index] -= 1
                    sol[len(sol) - 1] += abecedary[max_index]
    return ' '.join(sol)


t = int(raw_input())
for i in xrange(1, t + 1):
    parties = int(raw_input())
    senators = [int(x) for x in raw_input().split(' ')]
    print "Case #{}: {}".format(i, solve(parties, senators))
