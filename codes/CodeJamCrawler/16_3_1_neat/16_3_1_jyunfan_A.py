import sys
import numpy as np

def resolve(N, party):
    result = []
    while True:
        if sum(party) == 1:
            users = np.where(party)
            result.append(chr(65+users[0][0]))
            break
        elif sum(party) == 2:
            users = np.where(party)
            result.append(chr(65+users[0][0]) + chr(65+users[0][1]))
            break
        elif sum(party) == 3 and len(np.where(party==1)[0])==3:
            m = max(party)
            ev = np.where(party==m)[0]
            user = ev[0]
            result.append(chr(65+user))
            party[user] -= 1
        else:
            m = max(party)
            ev = np.where(party==m)[0]
            if len(ev) == 1:
                user = ev[0]
                result.append(chr(65+user))
                party[user] -= 1
            else:
                user = ev[0]
                party[user] -= 1

                user = ev[1]
                party[user] -= 1

                result.append(chr(65+ev[0])+chr(65+ev[1]))


    return result

T = int(sys.stdin.readline().strip())
for case in range(1, T+1):
    N = int(sys.stdin.readline().strip())
    party = (sys.stdin.readline().strip()).split()
    party = np.array([int(x) for x in party])
    answer = ' '.join(resolve(N,party))
    print('Case #%d: %s' % (case, answer))
    case += 1
