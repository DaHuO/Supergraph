infile = open('input.in','r')
outfile = open('output.out','w')


T = int(infile.readline())

for t in range(T):
    arr = infile.readline().split()
    K = int(arr[0])
    C = int(arr[1])
    S = int(arr[2])
    outfile.write('Case #' + str(t+1) + ': ')
    for i in range (0,S):
        outfile.write(str(i+1) + ' ')
    outfile.write('\n')

infile.close()
outfile.close()