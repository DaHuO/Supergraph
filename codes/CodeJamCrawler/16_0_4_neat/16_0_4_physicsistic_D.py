import sys

def solve(K,C,S):
    output = ''
    for i in range(S):
        output += str(i+1) + ' '
    return output

 
def io(filename):
    output = open(filename.split('.')[0]+'.out', 'w')
    with open(filename, 'r') as f:
        T = int(f.readline())
        for t in range(T):
            K, C, S = map(int,f.readline().rstrip('\n').split())
            string = "Case #{n}: {y}".format(n=t+1, y=solve(K, C, S))
            print string
            print "======================================================="
            output.writelines(string+'\n')   
 
if __name__ == '__main__':
    input_file = sys.argv[1]
    io(input_file)