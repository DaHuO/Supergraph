attempt_list = ['A-test','A-small-attempt0','A-large']
attempt = attempt_list[2]

import time
time.clock()

from operator import itemgetter

def solve(n, senators):

    alph = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    data = []
    for i in range(n):
        data.append([alph[i],senators[i]])
    data = sorted(data,key=itemgetter(1), reverse=True)
    total_left = sum(senators)
    evac_plan = ''

    # let's leave only the two major parties with equal members
    evac_plan += (data[0][0] + ' ') * (data[0][1] - data[1][1])
    data[0][1] = data[1][1]

    # let's evacuate all other parties
    for i in range(n-2):
        evac_plan += (data[i+2][0] + ' ') * data[i+2][1]

    # evacuate the two parties
    evac_plan += (data[0][0] + data[1][0] + ' ') * data[0][1]

    return evac_plan


def main():
    fin = open(attempt + '.in', 'r')
    fout = open(attempt + '.out','w')

    numcases = int(fin.readline())

    for casenum in range(1,numcases+1):
        n = int(fin.readline())
        senators = [int(i) for i in fin.readline().split()]
        fout.write('Case #' + repr(casenum) + ': ' + str(solve(n, senators)) + '\n')

    fin.close()
    fout.close()

main()
print(time.clock())