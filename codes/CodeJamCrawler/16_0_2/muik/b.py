import fileinput
f = fileinput.input()
T = int(f.readline())

def solve(S):
    count = 0
    for i in range(0, len(S)-1):
        if S[i] == S[i+1]:
            continue
        count += 1
    if S[-1] != '+':
        count += 1
    return count

for case in range(1, T+1):
    S = f.readline().strip()
    print "Case #%d: %d" % (case, solve(S))
