import math

numbers = [0,1,2,3,4,5,6,7,8,9]
cases = []
cased = []
casenum = []
i2 = 0
##b = {'one': 1, 'two': 2, 'three': 3}
p = 1
fileo = open('output.txt', 'w')

def validate(case):
    cases = []
    p = int(1)
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    cases.append(case)

    while True:

        q = str(case * p)
        x = len(q)
        cases.append(str(q))
        for i in range(x):
            cases.append(q[i])
        p+=1
        if numbers[0] in cases and numbers[2] in cases and numbers[3] in cases and numbers[4] in cases and numbers[5] in cases and numbers[6] in cases and numbers[7] in cases and numbers[8] in cases and numbers[9] in cases:
            cases = []
            cases.append(str(q))
            cased.append('Case #'+(str(i2))+': '+(str(q)))
            break
        elif q == str('0'):
        	cased.append('Case #'+(str(i2))+': '+'INSOMNIA')#case+1
        	break

   


T = int(raw_input())

for case in range(T):
	i2+=1
	case = int(raw_input(''))
	validate(case)

for i in range(len(cased)):
	print cased[i]
	fileo.write(cased[i]+'\n')