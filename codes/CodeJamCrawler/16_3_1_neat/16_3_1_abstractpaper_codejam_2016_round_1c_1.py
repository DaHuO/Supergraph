import string
import operator

T = int(raw_input())
alphabet = string.ascii_uppercase

for case in range(T):
    N = int(raw_input())
    Ni = []
    Ni = map(lambda x: int(x), raw_input().split())
    Nd = {alphabet[k]:v for k,v in enumerate(Ni)}
    sorted_Nd = sorted(Nd.items(), key=operator.itemgetter(1), reverse=True)

    evac = []
    while len(sorted_Nd) > 0:
        if len(sorted_Nd)%2==1 and sorted_Nd[0][1]==1:
            evac.append("%s" % (sorted_Nd[0][0]))
            sorted_Nd[0] = (sorted_Nd[0][0], sorted_Nd[0][1]-1)
            if sorted_Nd[0][1] == 0:
                sorted_Nd.pop(0)
        else:
            evac.append("%s%s" % (sorted_Nd[0][0], sorted_Nd[1][0]))
            sorted_Nd[0] = (sorted_Nd[0][0], sorted_Nd[0][1]-1)
            sorted_Nd[1] = (sorted_Nd[1][0], sorted_Nd[1][1]-1)
            if sorted_Nd[0][1] == 0 and sorted_Nd[1][1] == 0:
                del sorted_Nd[0:2]
            elif sorted_Nd[0][1] == 0:
                sorted_Nd.pop(0)
            elif sorted_Nd[1][1] == 0:
                sorted_Nd.pop(1)

        if len(sorted_Nd) > 2 and sorted_Nd[0][1] <= sorted_Nd[2][1]:
            sorted_Nd = sorted(sorted_Nd, key=lambda x: x[1], reverse=True)

    print "Case #%d: %s" % (case+1, ' '.join(evac).strip())