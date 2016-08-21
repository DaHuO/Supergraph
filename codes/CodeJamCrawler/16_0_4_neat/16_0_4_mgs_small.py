fid = open('input.txt')
T = fid.readline().strip()
fout = open('output.txt','w')

import numpy as np

#Index the query locations 0 through K^C-1, call the location j
#Imagine just one G, the hardest case.  There are locations 0,...,K locations
#for the G to be.

#Given a pair of locations in 0,K that we want to check for Gs, we can check C
#of them at once.  This function returns a location that will check those C.
#It will always be unique to the particular tuple given.
#x is a set of things we want to check (in np array)
#If we give a shorter array, should handle it gracefully
def test_index(x,C,K):
  return sum(np.multiply(K**(C-np.arange(len(x))-1),x))

#This just breaks up the locations we need into pairs, and finds the test
#location for each one
def get_idx(C,K):
    S = int(np.ceil(K/float(C)))
    test_pts = []
    for i in range(S):
        x = np.arange(i*C,min((i+1)*C,K))
        test_pts.append(test_index(x,C,K))
    return test_pts

for i,line in enumerate(fid):
    line = line.strip()
    if len(line)==0:
        continue
    K, C, S = [int(x) for x in line.split(' ')]
    if S < int(np.ceil(K/float(C))):
        out = 'IMPOSSIBLE'
    else:
      idx = get_idx(C,K)
      #As we convert to string, shift every index to one-indexed
      out = ' '.join([str(d+1) for d in idx])

    fout.write('Case #%d: %s\n' % (i+1, out))
