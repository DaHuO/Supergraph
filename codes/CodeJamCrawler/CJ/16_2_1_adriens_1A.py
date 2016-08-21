import sys

corresporder='ZWUXSVRHIO'

corresp = {
    'Z': ['ZERO', 0],
    'W': ['TWO', 2],
    'U': ['FOUR', 4],
    'X': ['SIX', 6],
    'S': ['SEVEN', 7],
    'V': ['FIVE', 5],
    'R': ['THREE', 3],
    'H': ['EIGHT', 8],
    'I': ['NINE', 9],
    'O': ['ONE', 1] }


def extractone(s):
    lst = list(s)
    for i in corresporder:
        if i in s:
           word = corresp[i][0]
	   for w in word:
               lst.remove(w)
           return [''.join(lst), corresp[i][1] ]
               

def do(s):
    numbers = []
    while(len(s)>0):
        s, n = extractone(s)
        numbers.append(n)
    numbers.sort()
    N = ''.join([str(n) for n in numbers])
    return N


T = int(sys.stdin.readline())
for i in range(T):
    s = sys.stdin.readline().strip()
    print "Case #%i:"%(i+1), do(s)

