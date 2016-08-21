inputF = open('D-small-attempt1.in', 'r')
output = open('D-small-attempt1.out', 'w')

numCases = int(inputF.readline())

# Simple trivial algorithm
for i in range(numCases):
    [k,c,s] = [int(x) for x in inputF.readline().split()]
    output.write('Case #' + str(i+1) + ': ')
    for j in range(k):
        output.write(str(j+1) + ' ')
    output.write('\n')
       

inputF.close()
output.close()
