#-------------------------------------------------------------------------------
# Name:        Google Code Jam 2016 - Qualifiers - Revenge of the Pancakes
#
# Author:      Ashish Nitin Patil
#
# Created:     09-04-2016
# Copyright:   (c) Ashish Nitin Patil 2016
# Licence:     New BSD License
#-------------------------------------------------------------------------------

T = int(input())

def min_flips_req(S=''):
    if S.find('-') == -1:
        return 0
    elif S.find('+') == -1:
        return 1
    if S.endswith('+'):
        return min_flips_req(S[:S.rfind('-')+1])
    else:
        return min_flips_req(S[:S.rfind('+')+1]) + 2

for test_case in range(1, T+1):
    S = input()
    min_flips = 0
    print("Case #{0}: {1}".format(test_case, min_flips_req(S)))
