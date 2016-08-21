# 2016 Africa Qualification Round - A. Counting Sheep
# https://code.google.com/codejam/contest/6254486/dashboard#s=p0

def build_flags():
    flags = {}
    for i in range(10):
        flags[i] = 1
    return flags

def solve(n, flags):
    if int(n) is 0:
        return 'INSOMNIA'

    result = 0
    
    while len(flags):
        result += n
        #print flags, result
        for digit in str(result):
            if flags.get(int(digit)):
                del flags[int(digit)]

    return result

#input, solve and output:
input = open('A-large.in', 'r')
output = open('A-large.out', 'w')

n_cases = int(input.readline())
for case in range(1, n_cases+1):
    n = int(input.readline())
    result = solve(n, build_flags())

    result_output = 'Case #%s: %s\n' %(case, result)
    #print result_output
    output.write(result_output)

input.close()
output.close()
