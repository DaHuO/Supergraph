'''
Created on 15 Apr 2016

@author: Andy
'''
digits = [(0,"ZERO",'Z'),
(2,'TWO','W'),
(8,"EIGHT",'G'),
(4, "FOUR", 'U'),
(5,"FIVE",'F'),
(6,'SIX','X'),
(9,'NINE','I'),
(1,'ONE','O'),
(3,'THREE','T'),
(7,'SEVEN','S')]

def solveIt(word):
    '''
    '''
    def getDigits(word):
        for digit in digits:
            while digit[2] in word:
                yield digit[0]
                for c in digit[1]:
                    idx = word.find(c)
                    if idx <0:
                        raise Exception("Failed to find:" + c + " in " + word )
                    word = word[:idx] + word[idx+1:]
    result = list(getDigits(word))
    return sorted(result) 

if __name__ == '__main__':
    with open('problem.txt') as fp:
        noOfProblems = int(fp.readline().strip())
        with open('solution.txt','w') as solution:
            for x in range(noOfProblems):
                result = solveIt(fp.readline().strip())
                answerLine = 'Case #{0}: {1}\n'.format(x+1,''.join(map(str,result)))
                print answerLine
                solution.write(answerLine)
