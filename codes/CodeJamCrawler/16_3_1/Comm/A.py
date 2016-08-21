import numpy as np
import operator

def solve():
    N = int(raw_input())
    partynum = {chr(i+65):int(x) for i,x in enumerate(raw_input().split(' '))}
    tot = sum(partynum.values())
    numparties = sum([1 if partynum[key] != 0 else 0 for key in partynum.keys()])
    output = []
    while (tot > 0):
        if numparties > 2:
            if tot == 2:
                counter = 0
                toremove = []
                
                for key in partynum.keys():
                    if counter < 2:
                        if partynum[key] > 0:
                            toremove.append(key)
                            counter += 1
                            partynum[key] -= 1
                    else:
                        break
                output.append(''.join(toremove))
                    
            elif tot == 3:
                counter = 0
                toremove = []
                
                for key in partynum.keys():
                    if counter < 1:
                        if partynum[key] > 0:
                            toremove.append(key)
                            counter += 1
                            partynum[key] -= 1
                    else:
                        break
                output.append(''.join(toremove))
            else:
                toremove = max(partynum.iteritems(), key=operator.itemgetter(1))[0]
                output.append(toremove)
                partynum[toremove] -= 1
        else:
            a = partynum['A']
            b = partynum['B']
            if a > b:
                output.append('A')
                partynum['A'] -= 1
            elif b > a:
                output.append('B')
                partynum['B'] -= 1
            elif a == b:
                partynum['A'] -= 1
                partynum['B'] -= 1
                output.append('AB')
        tot = sum(partynum.values())
            
    return ' '.join(output)


if __name__ == "__main__":
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
        output = solve()
        print "Case #{}: {}".format(i, output)