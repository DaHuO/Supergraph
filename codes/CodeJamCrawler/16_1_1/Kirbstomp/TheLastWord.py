input = open("input.txt","r+")
cases = int(input.readline())
solution = open("solve.txt","w")
caseNum = 1
def solve(word):
    newWord = []
    for x in list(word.strip()):
        if len(newWord)==0:
            newWord.append(x)

        else:
            if (x>=newWord[0]):
                newWord.insert(0,x)
            else:
                newWord.append(x)
    return ''.join(newWord)

for x in range(0,cases):
    ans = solve(input.readline())
    solution.write("Case #"+str(caseNum)+": "+ans+"\n")
    caseNum+=1