import sys

def solve(input_str):
    prev_sign = ''
    nflips = 0
    for si in input_str:
        if prev_sign == '':
            prev_sign = si
            continue
        if si != prev_sign:
            nflips += 1
            prev_sign = si
    if prev_sign == '-':
        nflips += 1
    return nflips

def main():
    num_cases = int(sys.stdin.readline())
    for i in xrange(num_cases):
        input_str = sys.stdin.readline().strip()
        outputi = solve(input_str)
        sys.stdout.write('Case #%i: %s\n'%(i+1, outputi))
    return


main()
