import sys

def get_answer():
    global inp
    t = inp.readline()
    k, c, s = map(int, t.split())
    return ' '.join(map(str, range(1, k + 1)))
    

inname = sys.argv[1]
outname = sys.argv[2]

out = open(outname, 'w')
inp = open(inname, 'r')
n = inp.readline()
for _ in range(int(n)):
    answer = get_answer()
    print('Case #{}: {}'.format(_ + 1, answer), file=out)
