import sys

def get_answer():
    global inp
    s = inp.readline()[::-1]
    flipped = 0
    answer = 0
    for c in s:
        if (c == '-' and not flipped) or (c == '+' and flipped):
            flipped = 1 - flipped
            answer += 1
    return answer

inname = sys.argv[1]
outname = sys.argv[2]

out = open(outname, 'w')
inp = open(inname, 'r')
n = inp.readline()
for _ in range(int(n)):
    answer = get_answer()
    print('Case #{}: {}'.format(_ + 1, answer), file=out)
