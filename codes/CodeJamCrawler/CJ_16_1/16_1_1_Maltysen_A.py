import fileinput
import framework
from itertools import product

for j, line in enumerate(list(fileinput.input())[1:]):
    S = line[:-1]
    k = S[0]
    S = S[1:]
    for l in S:
        if l >= k[0]:
            k = l + k
        else:
            k += l
    print("Case #{}: {}".format(j+1, k))
