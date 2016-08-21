import sys

def solve(input_str):
    K,C,S = [int(si) for si in input_str.split(' ')]
    C_1 = C - 1
    ind = 0
    cand_vec = []
    while True:
        wind = range(ind, ind + C)
        cand = sum( (wi % K) * (K ** ci) for (wi, ci) in zip(wind, range(C_1, -1, -1)))
        cand_vec.append(cand + 1)
        ind += C
        if ind >= K:
            break
    if len(cand_vec) > S:
        return "IMPOSSIBLE"
    return ' '.join(['%i'%xi for xi in cand_vec]) 

def main():
    num_cases = int(sys.stdin.readline())
    for i in xrange(num_cases):
        input_str = sys.stdin.readline().strip()
        outputi = solve(input_str)
        sys.stdout.write('Case #%i: %s\n'%(i+1, outputi))
    return


main()
