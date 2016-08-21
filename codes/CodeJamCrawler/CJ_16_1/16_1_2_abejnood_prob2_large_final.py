import csv, sys, random, math

def solve(N, f):
    counts = [0 for j in xrange(2501)]
    values = []
    
    for i in xrange(2 * N - 1):
        line_list = str(f.readline()).split()
        convert_to_ints = [ int(value) for value in line_list]
        for j in xrange(N):
            counts[ convert_to_ints[j]  ] = counts[ convert_to_ints[j] ] + 1

    for j in xrange(2501):
        if counts[j] % 2 != 0:
            values.append(j)

    sorted_vals = sorted(values)
    convert_back = [ str(value) for value in sorted_vals]
    return convert_back
    
    

target = open("prob2_output_large.txt", 'w')
with open('prob2_large.txt','r') as f:
    T = int(f.readline())    
    for i in xrange(T):
        N = int(f.readline())
        case_num = str(i+1)
        sol_str = 'Case #' + case_num +  ': ' + ' '.join( solve(N,f)  ) + '\n'
        target.write( str(sol_str) )
        
    






