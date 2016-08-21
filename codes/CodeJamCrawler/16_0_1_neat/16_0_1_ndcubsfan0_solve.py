import sys

def solve(input_str):
    def add_str(myset, Nstr):
        for si in Nstr.strip():
            myset.add(si)
    N = int(input_str)
    if N == 0:
        return 'INSOMNIA'
    myset = set()
    count = 0
    add_str(myset, input_str.strip()) 
    cur_num = N
    while len(myset) < 10:
        cur_num += N
        cur_num_str = str(cur_num)
        add_str(myset, cur_num_str) 
        if count > 200:
            raise RuntimeError()
    return cur_num_str

def main():
    num_cases = int(sys.stdin.readline())
    for i in xrange(num_cases):
        N = sys.stdin.readline()
        outputi = solve(N)
        sys.stdout.write('Case #%i: %s\n'%(i+1, outputi))
    return


main()
