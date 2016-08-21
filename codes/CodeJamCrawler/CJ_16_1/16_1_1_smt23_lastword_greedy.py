# Scan for the highest letter, from the left
# put all letters at the back until the highest letter

def solveProblem(letters):

    # remove \n from end of list
    letters.pop()

    ans = []
    ans.append(letters[0])
    letters = letters[1:]
    while len(letters) > 0:
        if letters[0] >= ans[0]:
            ans.insert(0,letters[0])
        else:
            ans.append(letters[0])
        letters = letters[1:]

    return ans

filename = 'A-large'
inFile = open(filename + '.in','r')
outFile = open(filename + '.out','w')

numCases = int(inFile.readline())

for i in range(0,numCases):

    ans = solveProblem(list(inFile.readline()))
    #print(ans)

    outFile.write('Case #' + str(i+1) + ': ')
    for x in ans:
        outFile.write(str(x))
    outFile.write('\n')
