__author__ = 'pavlovick'
import string
import numpy as np

def tot_senators(senators):
    return sum(senators)

def tot_parties(senators):
    return sum(x > 0 for x in senators)

def get_non_zero_idx(senators):
    return np.nonzero(senators)[0]


def evacuate(senators):
    senators = [int(senator) for senator in senators]
    exit_list=''
    while tot_senators(senators)>0:
        if tot_parties(senators)>2:
            idx = senators.index(max(senators))
            senators[idx]= senators[idx]-1
            party=string.uppercase[idx]
            exit_list= exit_list + party + " "
            print senators
        if tot_parties(senators)< 3:
            idxs = get_non_zero_idx(senators)
            non_zero_senators = [senators[idx] for idx in idxs]
            if  max(non_zero_senators) > min(non_zero_senators):
                idx = senators.index(max(senators))
                senators[idx]= senators[idx]-1
                party=string.uppercase[idx]
                exit_list= exit_list + party + " "
                print senators
            else:
                for idx in idxs:
                    senators[idx]= senators[idx]-1
                    exit_list = exit_list + string.uppercase[idx]
                exit_list = exit_list + " "
                print senators
    return exit_list






solution = open('solution.txt', 'w')
with open('test.txt') as f:
 N_tot= int(f.readline())
 count = 1
 while True:
     N= f.readline()
     plan = evacuate(f.readline().replace("\n","").split(' '))
     newLine = 'Case #'+ str(count) +': '+ plan +'\n'
     solution.write(newLine)
     count +=1