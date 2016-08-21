def parse_file(location):
    fin = open(location,'r')
    N = int(fin.readline().split('\n')[0])
    cases = [int(val.split('\n')[0]) for val in fin.readlines()]
    return N,cases
    
def check_numbers(n):
    ''' Return list of values we saw '''
    return list(set([int(v) for v in str(n)]))

def count_sheep(n):
    if n == 0:
        return 'INSOMNIA'
    vals_seen = set()
    i = 1
    while True:
        vals = check_numbers(i*n)
        for v in vals:
            vals_seen.add(v)
        if vals_seen == set([0,1,2,3,4,5,6,7,8,9]):
            break
        i += 1
    return i*n
    
filename = 'A-large.in'
N, cases = parse_file(filename)
outputs = []
for case in cases:
    outputs.append(count_sheep(case))

fout = open('output_large.txt','w')
for i,output in enumerate(outputs):
    fout.write('Case #' + str(i+1) + ': ' + str(output)+'\n')
fout.close()