'''
Created on 8 Apr 2016

@author: Andy
'''
def solveProblem(k,c,s):
    """
    """
    if s < k:
        return "IMPOSSIBLE"
    return " ".join(map(str,range(1,k+1)))

if __name__ == '__main__':
    with open('problem.txt') as fp:
        noOfProblems = int(fp.readline().strip())
        with open('solution4.txt','w') as solution:
            for x in range(noOfProblems):
                k,c,s = map(int,fp.readline().strip().split())
                result = solveProblem(k,c,s)
                print result
                solution.write('Case #{0}: {1}\n'.format(x+1,result))
