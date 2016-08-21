'''
Created on 8 Apr 2016

@author: Andy
'''
def solveProblem(initialValue):
    """
    """
    value = initialValue
    if value <= 0:
        return "INSOMNIA"
    remainingDigits = [str(x) for x in range(10)]
    
    while True:
        foundDigits = []
        for digit in remainingDigits:
            if digit in str(value):
                foundDigits.append(digit)
        for digit in foundDigits:
            remainingDigits.remove(digit)
        if len(remainingDigits) == 0:
            break
        value += initialValue

    return value

if __name__ == '__main__':
    with open('problem.txt') as fp:
        noOfProblems = int(fp.readline().strip())
        with open('solution1.txt','w') as solution:
            for x in range(noOfProblems):
                result = solveProblem(int(fp.readline().strip()))
                solution.write('Case #{0}: {1}\n'.format(x+1,result))
    