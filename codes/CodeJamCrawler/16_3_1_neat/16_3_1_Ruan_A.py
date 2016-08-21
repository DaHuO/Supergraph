# -*- coding: utf-8 -*-
"""
Created on Sun May 08 12:03:05 2016

@author: theronrp
"""

import numpy as np
import heapq
f = file('large.in', 'r')
fo = file('output.out', 'w')

numTestCases = int(f.readline())
party_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
party_dict = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7}
for test_case in range(0, numTestCases):
    num_of_parties = int(f.readline())
    party_count = map(float, str(f.readline()).split(' '))
    #party_count = np.array(party_count)
    total_members = sum(party_count)
    percent_representation = []
    for i in range (0, num_of_parties):
        percent_representation.append((party_count[i] / total_members))
    
    evacuation_plan = []        
    while total_members > 0:

        #Try evacuating 2
        
        found_evac = False
        for i in range(0, num_of_parties):
            for j in range(0, num_of_parties):
                possible_party_count = party_count[:]
                if party_count[i] > 0 and party_count[j] > 0:
                    possible_party_count[i] -= 1
                    if possible_party_count[j] == 0:
                        break
                    possible_party_count[j] -= 1
                    possible_total_members = sum(possible_party_count)
                    if possible_total_members == 0:
                        found_evac = True
                        evacuation_plan.append(party_names[i]+ party_names[j])
                        total_members = possible_total_members
                        break
                    
                    okay = True
                    for k in range (0, num_of_parties):
                        rep = possible_party_count[k] / possible_total_members
                        if rep > 0.5:
                            okay = False
                    if okay:
                        found_evac = True
                        evacuation_plan.append(party_names[i]+ party_names[j])
                        party_count = possible_party_count[:]
                        total_members = possible_total_members
                        break
            if found_evac:
                break

        #Try evacuating 1 only
        if not found_evac:
            for i in range(0, num_of_parties):
                possible_party_count = party_count[:]
                if party_count[i] > 0:
                    possible_party_count[i] -= 1
                    possible_total_members = sum(possible_party_count)
                    if possible_total_members == 0:
                        found_evac = True
                        evacuation_plan.append(party_names[i])
                        total_members = possible_total_members
                        break
                    
                    okay = True
                    for k in range (0, num_of_parties):
                        rep = possible_party_count[i] / possible_total_members
                        if rep > 0.5:
                            okay = False
                    if okay:
                        found_evac = True
                        evacuation_plan.append(party_names[i])
                        party_count = possible_party_count[:]
                        total_members = possible_total_members
                        break

    print ('CASE #' + str(test_case + 1) + ': ' + ' '.join(evacuation_plan))
    fo.write('CASE #' + str(test_case + 1) + ': ' + ' '.join(evacuation_plan) + '\n')
    
f.close()
fo.close()
        
    
    
            
        
    