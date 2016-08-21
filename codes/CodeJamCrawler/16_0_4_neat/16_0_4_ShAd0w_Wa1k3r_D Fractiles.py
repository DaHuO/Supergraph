#-------------------------------------------------------------------------------
# Name:        Google Code Jam 2016 - Qualifiers - Fractiles
#
# Author:      Ashish Nitin Patil
#
# Created:     10-04-2016
# Copyright:   (c) Ashish Nitin Patil 2016
# Licence:     New BSD License
#-------------------------------------------------------------------------------

T = int(input())

def tiles_to_uncover(K, C, S):
    # knowing that K=S
    if K == 1:
        return '1'
    elif S < K:
        return 'IMPOSSIBLE'
    else:
        return ' '.join(map(lambda x: str(int(x)), [(i-1)*(K**C-1)/(K-1)+1 for i in range(1,K+1)]))

for test_case in range(1, T+1):
    K, C, S = map(int, raw_input().split())
    print "Case #{0}: {1}".format(test_case, tiles_to_uncover(K, C, S))
