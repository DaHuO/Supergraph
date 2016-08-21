def parse_file(location):
    fin = open(location,'r')
    N = int(fin.readline().split('\n')[0])
    cases = [val.split('\n')[0] for val in fin.readlines()]
    return N,cases
    
def save_answers(location,values):
    fout = open(location,'w')
    for i,output in enumerate(values):
        fout.write('Case #' + str(i+1) + ': ' + str(output)+'\n')
    fout.close()
    
def solve_pancakes(string):
    ''' Strategy: count the number of sign changes, and add one if the final value is -. '''
    flips = 0
    for i in range(1,len(string)):
        if string[i] != string[i-1]:
            flips += 1
    if string[-1] == '-':
        flips += 1
    return flips

location_in = 'B-large.in'
location_out = 'output_large.txt'

N, cases = parse_file(location_in)

outputs = []
for case in cases:
    outputs.append(solve_pancakes(case))

save_answers(location_out,outputs)
