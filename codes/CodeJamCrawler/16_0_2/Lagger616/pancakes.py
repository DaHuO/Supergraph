def test(stack):
    if '-' not in stack:
        return 0
    elif '+' not in stack:
        return 1

    if stack[0] == '+':
        index = stack.index('-')
        stack2 = stack[0:index:-1]
        stack2 = stack2.replace('+', '-')
        stack = stack2 + stack[index:]
        return 1 + test(stack)

    if stack[0] == '-':
        index = stack.index('+')
        stack2 = stack[0:index:-1]
        stack2 = stack2.replace('-', '+')
        stack = stack2 + stack[index:]
        return 1 + test(stack)

f = open('B-large.in', 'r')
testsNumber = int(f.readline())
casesList = []
while testsNumber > 0:
    casesList.append(f.readline())
    testsNumber -= 1
f.close()

output = open('large-output.txt', 'w')

for case in range(len(casesList)):
    output.write('Case #' + str(case+1) + ': ' + str(test(casesList[case])) + '\n')
output.close()








