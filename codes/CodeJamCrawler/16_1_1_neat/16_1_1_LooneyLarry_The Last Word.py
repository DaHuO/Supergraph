# Google Code Jam 2016 1AA
def doCase(S):
    answer = ''
    for letter in S:
        if len(answer) > 0 and letter >= answer[0]:
            answer = letter + answer
        else:
            answer = answer + letter
    return answer

cases = int(raw_input())
for i in range(cases):
    print 'Case #{}: {}'.format(i+1, doCase((raw_input().strip())))
