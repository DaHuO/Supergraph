'''
Created on 8 Apr 2016

@author: Andy
'''
def solveProblem(input):
    """
    """
    input += '+'
    result = 0
    for i in range(0, len(input)-1):
        if input[i] != input[i+1]:
            result += 1
    return result



if __name__ == '__main__':
    with open('problem.txt') as fp:
        noOfProblems = int(fp.readline().strip())
        with open('solution2.txt','w') as solution:
            for x in range(noOfProblems):
                result = solveProblem(fp.readline().strip())
                answerLine = 'Case #{0}: {1}\n'.format(x+1,result)
                print answerLine
                solution.write(answerLine)
        