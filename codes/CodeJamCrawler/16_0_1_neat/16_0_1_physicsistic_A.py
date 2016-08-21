import sys

def solve_small(N):
    seen_digits = set()
    for i in range(1000):
        number = (i+1) * N
        for c in str(number):
            seen_digits.add(c)
        if len(seen_digits) == 10:
            return number
    return 'INSOMNIA'


def solve(N):
    if N == 0:
        return 'INSOMNIA'
    seen_digits = set()
    i = 0
    while True:
        number = (i+1) * N
        for c in str(number):
            seen_digits.add(c)
        if len(seen_digits) == 10:
            return number
        i += 1
 
def io(filename):
    output = open(filename.split('.')[0]+'.out', 'w')
    with open(filename, 'r') as f:
        T = int(f.readline())
        for t in range(T):
            N = int(f.readline().rstrip('\n'))
            string = "Case #{n}: {y}".format(n=t+1, y=solve(N))
            print string
            print "======================================================="
            output.writelines(string+'\n')   
 
if __name__ == '__main__':
    input_file = sys.argv[1]
    io(input_file)