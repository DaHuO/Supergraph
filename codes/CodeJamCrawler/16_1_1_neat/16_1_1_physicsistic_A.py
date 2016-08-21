import sys

def solve(S):
    words = [S[0]]
    for c in S[1:]:
        new_words = []
        for word in words:
            new_words.append(word+c)
            new_words.append(c+word)
        words = new_words
    words.sort()
    return words[-1] 
 
def io(filename):
    output = open(filename.split('.')[0]+'.out', 'w')
    with open(filename, 'r') as f:
        T = int(f.readline())
        for t in range(T):
            S = f.readline().rstrip('\n')
            string = "Case #{n}: {y}".format(n=t+1, y=solve(S))
            print string
            print "======================================================="
            output.writelines(string+'\n')   
 
if __name__ == '__main__':
    input_file = sys.argv[1]
    io(input_file)